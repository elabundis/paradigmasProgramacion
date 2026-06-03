" Choose a pdf viewer for 'tex' files processed with vimtex
let g:vimtex_view_method = 'skim'

" Don't open QuickFix for warning messages if no errors are present
let g:vimtex_quickfix_open_on_warning = 0

" Enable folding and formating features (via gq)
let g:vimtex_fold_enabled = 1
let g:vimtex_format_enabled = 1

" Don't check spelling inside latex comments
let g:tex_comment_nospell = 1  

" Disable conceal features (annoying)
let g:vimtex_syntax_conceal_disable = 1

" Compilation setup
let g:vimtex_compiler_latexmk = {
    \ 'aux_dir' : 'build',
    \ 'out_dir' : '',
    \ 'callback' : 1,
    \ 'continuous' : 1,
    \ 'executable' : 'latexmk',
    \ 'hooks' : [],
    \ 'options' : [
    \   '-verbose',
    \   '-file-line-error',
    \   '-synctex=1',
    \   '-interaction=nonstopmode',
    \   '-halt-on-error',
    \ ],
    \}


" Return focus to nvim after inverse search call from skim
function! s:TexFocusVim() abort
  " Replace `TERMINAL` with the name of your terminal application
  " Example: execute "!open -a iTerm"  
  " Example: execute "!open -a Alacritty"
  silent execute "!open -a iTerm"
  redraw!
endfunction

augroup vimtex_event_focus
  au!
  au User VimtexEventViewReverse call s:TexFocusVim()
augroup END
