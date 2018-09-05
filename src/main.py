#!/usr/bin/env python

import argparse
import os
import jinja2
import jinja2.ext

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(PROJECT_DIR, 'template')
GENERATED_DIR = os.path.join(PROJECT_DIR, 'generated')


class StoreDictKeyPair(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self._nargs = nargs
        super(StoreDictKeyPair, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        result = {}
        for kv in values:
            k, v = kv.split('=')
            result[k] = v
        setattr(namespace, self.dest, result)


class RaiseExtension(jinja2.ext.Extension):
    tags = set(['raise'])

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        message_node = parser.parse_expression()
        return jinja2.nodes.CallBlock(
            self.call_method('_raise', [message_node], lineno=lineno),
            [], [], [], lineno=lineno
        )

    def _raise(self, msg, caller):
        raise jinja2.exceptions.TemplateRuntimeError(msg)


def render(name, template_name, params):
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR)
    template_environment = jinja2.Environment(loader=template_loader, extensions=[RaiseExtension])
    template = template_environment.get_template(template_name)
    result = template.render(**params)

    output_dir = os.path.join(GENERATED_DIR, name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    open(os.path.join(output_dir, 'Dockerfile'), 'w').write(result)


def main():
    parser = argparse.ArgumentParser(description='generate dockerfile')
    parser.add_argument('--name', required='true', dest='name', action='store', help='name for docker image')
    parser.add_argument('--template', required='true', dest='template', action='store', help='template name to be rendered')
    parser.add_argument('--params', required='true', dest='params', action=StoreDictKeyPair, nargs='+', metavar='KEY=VALUE', help='parameters to be passed to template')
    args = parser.parse_args()
    render(args.name, args.template, args.params)

if __name__ == '__main__':
    main()
