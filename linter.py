from SublimeLinter.lint import PythonLinter, WARNING


class Darglint(PythonLinter):
    cmd = ('darglint', '--verbosity', '2', '${file}', '${args}')
    regex = r'^.+?:(?P<near>.+):(?P<line>\d+): (?P<code>[IS]\d+): (?P<message>.+)'
    multiline = True
    defaults = {
        'selector': 'source.python',
        'default_type': WARNING,
        'tempfile_suffix': 'py',
        '--docstring-style': 'google',
    }
