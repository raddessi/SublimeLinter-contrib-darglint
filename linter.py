from SublimeLinter.lint import PythonLinter


class Darglint(PythonLinter):
    cmd = ('darglint', '${args}', '-')
    regex = r'^.+?:(?P<function>.+):(?P<line>\d+): (?:(?P<interface>I\d+)|(?P<style>S\d+)): (?P<message>.+)'
    multiline = True
    defaults = {
        'selector': 'source.python',
    }
