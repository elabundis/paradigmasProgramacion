nnoremap <C-p> :Files<CR>
nnoremap <F2> :Rg<CR>
let $BAT_THEME='gruvbox-light'

" Have ripgrep only look at file contents when searching
" and not include the filepath in the search
command! -bang -nargs=* Rg call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case ".shellescape(<q-args>), 1, {'options': '--delimiter : --nth 4..'}, <bang>0) 
