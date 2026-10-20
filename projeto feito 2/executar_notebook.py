"""Executa as células em Python e grava um notebook com saídas reais, sem servidor Jupyter."""
from pathlib import Path
import os, sys, json, io, contextlib, base64, traceback

root = Path(__file__).resolve().parent
os.chdir(root)
text = (root/'experimento.py').read_text(encoding='utf-8')
cells = []
for part in text.split('# %%'):
    if not part.strip(): continue
    markdown = part.startswith(' [markdown]')
    lines = part.splitlines()[1:]
    if markdown:
        source = '\n'.join(line[2:] if line.startswith('# ') else ('' if line=='#' else line) for line in lines).strip()
        cells.append({'cell_type':'markdown','metadata':{},'source':source})
    else:
        source = '\n'.join(lines).strip()
        cells.append({'cell_type':'code','metadata':{},'source':source,'execution_count':None,'outputs':[]})
install = {'cell_type':'code','metadata':{},'source':'# Execute no Colab. Na execução local registrada, as dependências já estavam instaladas.\n%pip -q install tensorflow keras numpy scipy matplotlib scikit-learn',
           'execution_count':None,'outputs':[]}
cells.insert(1,install)
nb = {'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},
                              'language_info':{'name':'python','version':sys.version.split()[0]},
                              'execution_note':'Células executadas sequencialmente em Python local; instalação Colab não executada.'},
      'nbformat':4,'nbformat_minor':4}
target = root/'Projeto_Grupo4.ipynb'
scope = {'__name__':'__main__'}
import IPython.display
current_outputs = []
def capture_display(obj):
    data = obj._repr_png_() if hasattr(obj,'_repr_png_') else None
    if data:
        if isinstance(data,tuple): data=data[0]
        encoded = data if isinstance(data,str) else base64.b64encode(data).decode()
        current_outputs.append({'output_type':'display_data','metadata':{},'data':{'image/png':encoded,'text/plain':['Figura gerada na execução.']}})
    else:
        print(str(obj))
IPython.display.display = capture_display
count = 0
log = root/'resultados'/'execucao.log'
log.parent.mkdir(exist_ok=True)
with log.open('w',encoding='utf-8') as logfile:
    for cell in cells:
        if cell['cell_type']!='code' or cell is install: continue
        count += 1
        print(f'Executando célula {count}',flush=True)
        current_outputs = []
        stdout = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stdout):
                exec(compile(cell['source'],f'notebook_celula_{count}','exec'),scope)
        except Exception:
            print(stdout.getvalue(),flush=True)
            raise
        content = stdout.getvalue()
        logfile.write(f'\nCELULA {count}\n'+content); logfile.flush()
        cell['execution_count']=count
        cell['outputs']=([{'output_type':'stream','name':'stdout','text':content}] if content else [])+current_outputs
        target.write_text(json.dumps(nb,ensure_ascii=False,indent=1),encoding='utf-8')
        print(f'Célula {count} concluída; {len(current_outputs)} figuras.',flush=True)
print('Notebook executado e salvo:',target,flush=True)
