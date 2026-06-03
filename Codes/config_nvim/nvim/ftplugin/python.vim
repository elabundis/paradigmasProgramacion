" Deal with <EOL> character
setlocal fileformat=unix

" PEP 8 indentation
setlocal tabstop=4
setlocal softtabstop=4
setlocal shiftwidth=4
setlocal textwidth=79
setlocal expandtab
setlocal autoindent  " already set in nvim but it doesn't hurt

" Show area where code can go without violating PEP 8
setlocal colorcolumn=+1

" Automatically flag unnecessary whitespace
call HighlightExtraSpaces()

" Remove whitespace at line ends on save
autocmd BufWritePre <buffer> call CleanExtraSpaces()
