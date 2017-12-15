"""Grep for TODOS."""
# ==============================================================================
#  File: todo.py
#  Author: Clay Dunston <dunstontc@gmail.com>
#  License: MIT license
#  Last Modified: 2017-12-07
# ==============================================================================

import re
import subprocess
from .base import Base
# from denite import util


# Based off of a script by @chemzqm in denite-git
def run_search(command, options, pattern, location):
    """Run grep, or the fastest available alternative.

    Arguments
    ---------
    command  : str
        The search engine to use
    options  : list
        Options to pass to the engine. Can be a list
    pattern  : str
        The RegEx to search for
    location : str
        The target directory

    Returns
    -------
    list     : The utf-8 decoded search results

    """
    try:
        p = subprocess.run(f"{command} {' '.join(options)} \"{pattern}\" {location}",
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           shell=True)
    except subprocess.CalledProcessError:
        return []
    return p.stdout.decode('utf-8').split('\n')


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name        = 'todo'
        self.kind        = 'file'
        self.matchers    = ['matcher_fuzzy']
        self.sorters     = ['sorter_rank']
        # self.syntax_name = 'deniteSource_Todos'
        self.vars = {
            'command' : 'ag',
            'options' : ['-s','--nocolor', '--nogroup', '--vimgrep'],
            'input'   : "\s(BUG|FIXME|HACK|TODO|XXX)\:\s",
            'encoding': 'utf-8'
        }

    def on_init(self, context):
        # context['is_async'] = True
        a = self.vars['command']
        b = self.vars['options']
        c = self.vars['input']
        d = self.vim.call('getcwd')

        context['todos'] = run_search(a, b, c, d)

    def gather_candidates(self, context):
        # cur_dir = self.vim.call('getcwd')
        cur_dir_len     = len(self.vim.call('getcwd'))
        path_pattern    = re.compile(r'(^.*?)(?:\:.*$)', re.M)
        # line_pattern = re.compile(r'(?:\:)(\d*)(?:\:)', re.M)
        line_pattern    = re.compile(r'(?:\:)(\d*)(?:\:)(\d*)', re.M)
        # content_pattern = re.compile(r'(?:\:\d*\:\d*\:\s*)(.*$)', re.M)
        content_pattern = re.compile(r'(TODO|FIXME|XXX)+(.*$)', re.M)

        candidates = []

        for item in context['todos']:
            try:
                 todo_path = path_pattern.search(item).group(1)
            except AttributeError:
                 todo_path = ''

            try:
                item_line = line_pattern.search(item)  # TODO: does it make a difference if this is defined before the try/except blocks?
                todo_line = item_line.group(1)
                todo_col  = item_line.group(2)
                todo_pos  = f'[{todo_line}:{todo_col}]'
            except AttributeError:
                todo_line = ''
                todo_pcol = ''
                todo_pos  = ''

            try:
                todo_content = content_pattern.search(item).group(0)
            except AttributeError:
                todo_content = ''

            if item:
                candidates.append({
                    'word':         item,
                    'abbr':         '{:>} {:>} {:>}'.format(todo_path[cur_dir_len:], todo_pos, todo_content, ),
                    'action__path': todo_path,
                    'action__line': todo_line,
                    'action__col':  todo_col,
                })

        return candidates

    def define_syntax(self):
        self.vim.command(r'syntax match deniteSource_Todo /^.*$/ containedin=' + self.syntax_name)
        # self.vim.command(r'syntax match deniteSource_Todo_Path /^\s\zs\S*\ze/ contained '
        # self.vim.command(r'syntax match deniteSource_Todo_Path /\zs\S*\ze\s*--.*$/ contained '
        self.vim.command(r'syntax match deniteSource_Todo_Path /\v%(^\s)(\w|\.|\/)*/ contained '
                         r'containedin=deniteSource_Todo')
        self.vim.command(r'syntax match deniteSource_Todo_Noise /\S*\%\(--\)\s/ contained '
                         r'containedin=deniteSource_Todo')
        self.vim.command(r'syntax match deniteSource_Todo_Word /\v(BUG|FIXME|HACK|NOTE|OPTIMIZE|TODO|XXX)\:/ contained '
                         r'containedin=deniteSource_Todo')
        self.vim.command(r'syntax match deniteSource_Todo_Pos /\d\+\(:\d\+\)\?/ contained '
                         r'containedin=deniteSource_Todo')
        # self.vim.command(r'syntax match deniteSource_Todo_Content /^.\{-}\ze\:/ contained '
        #                  r'containedin=deniteSource_Todo')

    def highlight(self):
        self.vim.command('highlight default link deniteSource_Todo Normal')
        self.vim.command('highlight default link deniteSource_Todo_Noise Comment')
        self.vim.command('highlight default link deniteSource_Todo_Path Directory')
        self.vim.command('highlight default link deniteSource_Todo_Pos Number')
        self.vim.command('highlight default link deniteSource_Todo_Word Type')


    # def convert(self, val, context):
    #     bufnr = val['bufnr']
    #     line = val['lnum'] if bufnr != 0 else 0
    #     col = val['col'] if bufnr != 0 else 0
    #     fname = "" if bufnr == 0 else self.vim.eval('bufname(' + str(bufnr) + ')')
    #     word = '{fname} |{location}| {text}'.format(
    #         fname=fname,
    #         location='' if line == 0 and col == 0 else '%d col %d' % (line, col),
    #         text=val['text'])
    #
    #     return {
    #         'word': word,
    #         'action__path': fname,
    #         'action__line': line,
    #         'action__col': col,
    #         'action__buffer_nr': bufnr,
    #         }
