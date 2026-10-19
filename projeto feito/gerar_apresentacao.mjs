import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {Presentation,PresentationFile} from 'file:///C:/Users/danie/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';
const root=path.dirname(fileURLToPath(import.meta.url));
process.env.RUNTIME_NODE_MODULES='C:/Users/danie/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const skill='C:/Users/danie/.codex/plugins/cache/openai-primary-runtime/presentations/26.1015.12040/skills/presentations';
const {finalizePresentation,applyPresentationChartFont}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')));
const build=path.join(root,'.build-slides');await fs.mkdir(build,{recursive:true});
const read=async n=>JSON.parse(await fs.readFile(path.join(root,'resultados',n),'utf8'));
const val=await read('validacao.json'),test=await read('teste.json'),hist=await read('historicos.json');
const P=Presentation.create({slideSize:{width:1280,height:720}});
const navy='#123F5D',teal='#157C80',body='#243746',gray='#52616B';
function txt(s,t,x,y,w,h,size=28,color=body,bold=false){
 const a=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 a.text=t;a.text.style={typeface:'Arial',fontSize:size,color,bold};return a;
}
function slide(title,owner,notes){
 const s=P.slides.add();s.background.fill='#FFFFFF';
 txt(s,title,64,42,1152,92,44,navy,true);
 txt(s,owner,64,655,1070,30,18,gray);
 txt(s,String(P.slides.items.length),1170,655,50,30,18,gray);
 s.speakerNotes.text=notes;return s;
}
function table(s,rows,x,y,w,h,widths){
 const t=s.tables.add({rows:rows.length,columns:rows[0].length,left:x,top:y,width:w,height:h,columnWidths:widths,values:rows});
 for(let r=0;r<rows.length;r++)for(let c=0;c<rows[0].length;c++){
   const cell=t.getCell(r,c);cell.fill=r===0?'#E1EFF3':r%2?'#FFFFFF':'#F5F8FA';
   cell.text.style={typeface:'Arial',fontSize:24,color:body,bold:r===0};
 }
 t.borders.assign({fill:'#D6E1E7',width:0.5,style:'solid'});return t;
}
async function image(s,name,x,y,w,h){
 const b=await fs.readFile(path.join(root,'resultados',name));
 s.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType:'image/png',alt:name,fit:'contain',position:{left:x,top:y,width:w,height:h}});
}
let s=slide('Reconhecimento de caracteres\nalfanuméricos','Grupo 4 | IASEG | Deep Learning | 19/10/2026',
 'Bruno Groppo, 1 minuto. Abrir com o problema: um caractere binário isolado entra, uma classe sai. Explicar que não se trata de um leitor completo de placas. Fonte: respostas das sessões e Descrição do Projeto.');
txt(s,'Uma imagem de 20 × 16 pixels. Uma classe entre 0-9 e A-Z.',64,236,1110,100,34,teal);
txt(s,'Bruno Groppo · Bruno Pimentel · Reynato Junior\nWallace Jardim · Daniel Gil',64,460,1100,90,25,gray);

s=slide('Problema e referência de comparação','Bruno Groppo | 2 minutos',
 'Explicar classificação multiclasse e por que uma CNN pode aprender traços. Baseline: frequência calculada no treino, empate resolvido pelo menor índice (0). Fonte: experimento.py, validacao.json. Não afirmar que basta superar um baseline constante para provar superioridade a outros métodos.');
txt(s,'Entrada',64,166,300,50,30,teal,true);txt(s,'Um caractere isolado, binário,\ncom orientação já definida.',64,226,520,110,30);
txt(s,'Saída',680,166,400,50,30,teal,true);txt(s,'36 pontuações softmax.\nEscolhemos a maior.',680,226,520,110,30);
txt(s,'Baseline: sempre prever 0',64,406,1100,55,36,navy,true);
txt(s,'6 acertos em 217 imagens de validação: 2,76%.\nUma MLP adicional compara a CNN com uma rede densa.',64,486,1120,100,30);

s=slide('Binary Alpha Digits','Bruno Pimentel | 1 minuto e 30 segundos',
 'Mostrar alguns caracteres e explicar 1.404 imagens, 39 por classe e um canal. Fonte: https://www.tensorflow.org/datasets/catalog/binary_alpha_digits ; https://cs.nyu.edu/home/people/in_memoriam/roweis/data.html . Os exemplos vêm apenas do treino, figura amostras.png.');
txt(s,'1.404 imagens · 36 classes · 39 exemplos por classe',64,145,1120,50,30,teal);
await image(s,'amostras.png',150,210,980,408);

s=slide('Cópias idênticas ficam no mesmo conjunto','Bruno Pimentel | 1 minuto e 30 segundos',
 'A auditoria encontrou 1.363 imagens únicas, 39 grupos repetidos e 38 grupos conflitantes 0/O. Todas as imagens de 0 coincidem com O. Agrupar pelo hash antes de separar impede vazamento de cópias. Grupos são estratificados pela combinação de rótulos, seed 42. Fonte: auditoria.json, contagens.json, duplicatas.json. Sem escritor identificado, não garantimos independência por pessoa.');
txt(s,'As imagens de 0 e O são iguais, com rótulos diferentes.\nO hash dos pixels define os grupos da divisão.',64,155,1140,110,30);
table(s,[['Conjunto','Imagens','Padrões únicos'],['Treino','971','943'],['Validação','217','210'],['Teste','216','210']],64,305,1152,260,[480,336,336]);
txt(s,'Seed 42 · Nenhuma cópia exata atravessa os conjuntos',64,592,1100,40,25,teal);

s=slide('Arquitetura da CNN','Reynato Junior | 2 minutos',
 'Explicar convolução, filtro compartilhado, pooling, Flatten e Dense. A dimensão do lote fica fora do input_shape. Conv2D usa padding same. Fontes: aula4 pp. PDF 129-140, aula5 p. PDF 49, experimento.py e CNN_Dropout_arquitetura.txt.');
table(s,[['Etapa','Saída por imagem'],['Entrada binária','20 × 16 × 1'],['Conv2D(16, 3, same, ReLU) + MaxPool','10 × 8 × 16'],['Conv2D(32, 3, same, ReLU) + MaxPool','5 × 4 × 32'],['Flatten + Dense(64, ReLU)','64'],['Dropout(0,3), só na melhoria','64'],['Dense(36, softmax)','36']],64,155,1152,420,[830,322]);
txt(s,'48.164 parâmetros nas duas CNNs; Dropout não adiciona pesos.',64,598,1120,40,24,teal);

s=slide('Treinamento e seleção','Reynato Junior | 1 minuto',
 'Sparse categorical crossentropy combina rótulo inteiro com saída softmax. Adam ajusta os pesos. EarlyStopping restaura a menor val_loss. A acurácia de validação escolhe a rede entre as configurações. Fontes: aula3 pp. PDF 50-64, aula5, https://keras.io/api/callbacks/early_stopping/ , configuracao.json.');
txt(s,'Adam: taxa 0,001\nBatch: 32 imagens\nLimite: 80 épocas',64,170,515,180,32);
txt(s,'Perda: entropia cruzada\nRótulos inteiros (sparse)\nMétrica principal: acurácia',680,170,520,180,32);
txt(s,'EarlyStopping: dez épocas sem reduzir val_loss.\nRestaurar os pesos da melhor época.',64,410,1120,100,32,navy,true);
txt(s,'Selecionar pela validação. Avaliar no teste somente ao final.',64,561,1130,60,28,teal);

s=slide('Dropout melhorou a validação nesta execução','Wallace Jardim | 1 minuto e 30 segundos',
 'Comparação feita nos mesmos 217 registros de validação. CNN inicial 160 acertos, CNN Dropout 168. Ganho de oito acertos, 3,69 pontos percentuais. Não houve teste de significância nem múltiplas sementes. Fonte: validacao.json.');
const chart=s.charts.add('bar',{position:{left:64,top:160,width:1152,height:390},categories:['Baseline','MLP','CNN inicial','CNN Dropout'],
 series:[{name:'Acurácia de validação',values:Object.values(val).map(v=>Number(v.accuracy.toFixed(10))),fill:teal}],barOptions:{direction:'column'},hasLegend:false,
 yAxis:{min:0,max:1,numberFormatCode:'0%',textStyle:{fontSize:22},majorGridlines:{fill:'#D6E1E7',width:1}},xAxis:{textStyle:{fontSize:24}},
 dataLabels:{showValue:true,position:'outEnd',numberFormatCode:'0.00%',textStyle:{fontSize:24,color:navy}}});
applyPresentationChartFont(chart,{fontFamily:'Arial'});
txt(s,'CNN inicial: 73,73% → CNN Dropout: 77,42%\nA melhoria foi acrescentar Dropout(0,3); o restante foi mantido.',64,566,1130,75,27,navy);

s=slide('Perda de treino e validação','Wallace Jardim | 1 minuto e 30 segundos',
 'Os gráficos têm todas as épocas, com eixos numéricos. Valores arredondados a seis casas para compatibilidade com a planilha incorporada. CNN inicial: menor val_loss 0,840 na época 10, parou em 20. Dropout: 0,689 na época 29, parou em 39. Mesmo com Dropout há separação entre treino e validação. Não confundir menor val_loss com maior val_accuracy. Fonte: historicos.json e execucoes.json.');
for(const [i,name] of ['CNN inicial','CNN Dropout'].entries()){
 const h=hist[name];const xs=h.loss.map((_,j)=>j+1);const c=s.charts.add('scatter',{position:{left:64+i*590,top:166,width:552,height:370},title:name,titleTextStyle:{fontSize:27},scatterOptions:{style:'line'},
 series:[{name:'Treino',xValues:xs,values:h.loss.map(v=>Number(v.toFixed(6))),line:{fill:navy,width:3}},{name:'Validação',xValues:xs,values:h.val_loss.map(v=>Number(v.toFixed(6))),line:{fill:'#D97706',width:3}}],
 hasLegend:true,legend:{position:'bottom',textStyle:{fontSize:20}},
 xAxis:{min:0,max:i===0?20:40,majorUnit:i===0?5:10,title:'Época',textStyle:{fontSize:20}},yAxis:{min:0,max:4,title:'Perda',textStyle:{fontSize:20},majorGridlines:{fill:'#D6E1E7',width:1}}});
 applyPresentationChartFont(c,{fontFamily:'Arial'});
}
txt(s,'Pesos restaurados: época 10 na CNN inicial; época 29 com Dropout.\nA validação estabiliza enquanto a perda de treino continua caindo.',64,574,1140,75,26);

s=slide('Teste final: 178 acertos em 216 imagens','Daniel Gil | 2 minutos',
 'Somente baseline e CNN selecionada foram avaliados no teste. CNN Dropout: accuracy 82,41%, macro-F1 0,817. Matriz completa no relatório. O foi previsto como 0 em quatro casos; S como 5 em dois. O recall de O é 1/6, e K e S 3/6. A ambiguidade 0/O impõe pelo menos seis erros no teste. Fontes: teste.json, metricas_por_classe.json, principais_confusoes.json e previsoes_teste.npz.');
table(s,[['Modelo','Acurácia','Macro-F1'],['Baseline','2,78%','0,002'],['CNN Dropout','82,41%','0,817']],64,152,1152,180,[500,326,326]);
await image(s,'acertos_erros.png',64,360,760,268);
txt(s,'38 erros\n\nO → 0: 4 casos\nS → 5: 2 casos',865,375,350,210,27,navy);

s=slide('Uso pretendido e limitações','Daniel Gil | 1 minuto',
 'Fechar com o que foi aprendido: comparação controlada e dados importam. Uso didático ou sugestão de transcrição com revisão humana. Não existe confiabilidade operacional demonstrada. Confirmar Colab limpo, aprovação do dataset e do grupo antes da entrega. Fontes: relatório seções 5 e 6; Descrição do Projeto; Modelo de Relatório.');
txt(s,'Demonstração de caracteres isolados, com revisão humana.',64,165,1120,85,36,teal,true);
txt(s,'0/O: pixels idênticos, rótulos conflitantes.\nPoucos exemplos por classe e uma única divisão.\nSem avaliação em fotografias, placas ou documentos reais.',64,294,1140,190,31);
txt(s,'Próximo passo: validar em dados externos e medir quando o modelo\ndeve se abster, antes de propor qualquer aplicação operacional.',64,525,1140,100,28,navy);

for(const [i,s] of P.slides.items.entries()){
 const png=await P.export({slide:s,format:'png',scale:1});
 await fs.writeFile(path.join(build,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
}
const candidate=path.join(build,'candidate.pptx');await (await PresentationFile.exportPptx(P)).save(candidate);
await fs.mkdir(path.join(build,'final'),{recursive:true});
const finalized=path.join(build,'final',`Apresentacao_${Date.now()}.pptx`);
await finalizePresentation({workspaceDir:root,candidatePath:candidate,finalPath:finalized,
 pythonExecutable:'C:/Users/danie/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',... [4,5,9].flatMap(n=>['--require-native-table-slide',String(n)])],
 requiredNativeTableOwnerSlides:[4,5,9],requiredNativeChartOwnerSlides:[7,8],materializeLiteralChartWorkbooks:true,
 fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,receiptPath:path.join(build,path.basename(finalized)+'.validation.json')});
await fs.copyFile(finalized,path.join(root,'Apresentacao_Grupo4.pptx'));
console.log('Apresentação finalizada.');
