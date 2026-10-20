import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {Presentation,PresentationFile} from 'file:///C:/Users/danie/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';

const root=path.dirname(fileURLToPath(import.meta.url));
process.env.RUNTIME_NODE_MODULES='C:/Users/danie/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const skill='C:/Users/danie/.codex/plugins/cache/openai-primary-runtime/presentations/26.1015.12040/skills/presentations';
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')));
const build=path.join(root,'.build-slides-simple');
await fs.mkdir(build,{recursive:true});
const P=Presentation.create({slideSize:{width:1280,height:720}});
const navy='#123F5D',teal='#157C80',body='#243746',gray='#52616B';

function txt(s,value,x,y,w,h,size=30,color=body,bold=false){
  const shape=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},
    fill:'none',line:{fill:'none',width:0}});
  shape.text=value;
  shape.text.style={typeface:'Arial',fontSize:size,color,bold};
  return shape;
}
function slide(title,owner,notes){
  const s=P.slides.add();
  s.background.fill='#FFFFFF';
  txt(s,title,64,40,1152,102,43,navy,true);
  txt(s,owner,64,657,1080,28,18,gray);
  txt(s,String(P.slides.items.length),1170,657,48,28,18,gray);
  s.speakerNotes.text=notes;
  return s;
}
function table(s,rows,x,y,w,h,widths){
  const t=s.tables.add({rows:rows.length,columns:rows[0].length,
    left:x,top:y,width:w,height:h,columnWidths:widths,values:rows});
  for(let r=0;r<rows.length;r++)for(let c=0;c<rows[0].length;c++){
    const cell=t.getCell(r,c);
    cell.fill=r===0?'#E1EFF3':r%2?'#FFFFFF':'#F5F8FA';
    cell.text.style={typeface:'Arial',fontSize:23,color:body,bold:r===0};
  }
  t.borders.assign({fill:'#D6E1E7',width:0.5,style:'solid'});
}
async function picture(s,name,x,y,w,h){
  const bytes=await fs.readFile(path.join(root,'resultados',name));
  s.images.add({blob:bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),
    contentType:'image/png',alt:name,fit:'contain',
    position:{left:x,top:y,width:w,height:h}});
}

let s=slide('Reconhecimento de letras e números',
  'Grupo 4 | Disciplina 3 | 19/10/2026',
  'Bruno Groppo. Dizer que a tarefa é classificar um caractere isolado. Fonte: Descrição do Projeto e notebook do projeto.');
txt(s,'Uma imagem de 20 × 16 pixels.\nUma resposta entre 36 classes.',64,227,1120,155,39,teal,true);
txt(s,'Bruno Groppo · Bruno Pimentel · Reynato Junior\nWallace Jardim · Daniel Gil',
  64,480,1120,90,27,gray);

s=slide('Problema e referência simples','Bruno Groppo | 2 minutos',
  'Explicar entrada, saída e a referência de prever sempre 0. Fonte: notebook do projeto; Descrição do Projeto, seção de experimentos.');
txt(s,'Entrada',64,170,510,55,31,teal,true);
txt(s,'Uma imagem com um único\nnúmero ou letra maiúscula.',64,226,535,115,31);
txt(s,'Saída',680,170,500,55,31,teal,true);
txt(s,'Escolha de uma entre\n36 classes possíveis.',680,226,500,115,31);
txt(s,'Referência: prever sempre 0',64,402,1100,55,35,navy,true);
txt(s,'Acertou 6 de 217 imagens de validação: 2,76%.',64,478,1120,80,30);

s=slide('Os dados do projeto','Bruno Pimentel | 1 minuto e 30 segundos',
  'A base escolhida foi Binary Alpha Digits. São 1.404 imagens, 39 por classe. Exemplos vêm do treino. Fonte: notebook do projeto e arquivo público da Universidade de Nova York.');
txt(s,'1.404 imagens · 36 classes · 39 imagens por classe',64,145,1120,54,30,teal);
await picture(s,'amostras.png',155,213,970,405);
txt(s,'MAT (arquivo de dados em formato MATLAB).',64,620,1000,25,18,gray);

s=slide('Como dividimos os dados','Bruno Pimentel | 1 minuto e 30 segundos',
  'Há imagens idênticas com rótulos 0 e O. Mantivemos cópias no mesmo conjunto para evitar vazamento de dados. Fonte: notebook do projeto; aula 3 sobre vazamento.');
txt(s,'Imagens iguais com rótulos 0 e O ficaram juntas.\nNenhuma cópia exata passa de um conjunto para outro.',
  64,150,1140,120,30);
table(s,[['Conjunto','Imagens','Uso'],
  ['Treino','971','Ajustar a rede'],
  ['Validação','217','Escolher a rede'],
  ['Teste','216','Avaliar no final']],64,308,1152,276,[410,225,517]);
txt(s,'Não temos informação sobre quem escreveu os caracteres.',64,599,1130,40,25,teal);

s=slide('Como a rede classifica a imagem','Reynato Junior | 2 minutos',
  'As camadas convolucionais procuram padrões; a redução diminui a imagem; a saída escolhe uma classe. Fonte: aula 4, notebook e PDF (formato portátil de documento); notebook do projeto.');
table(s,[['Etapa','O que acontece'],
  ['Imagem','20 × 16 pixels, valores 0 ou 1'],
  ['Duas convoluções','Procuram traços e curvas'],
  ['Duas reduções','Diminuem o tamanho dos dados'],
  ['Camada densa','Combina o que foi encontrado'],
  ['Saída softmax','Escolhe uma entre 36 classes']],
  64,155,1152,425,[440,712]);
txt(s,'A segunda versão acrescenta Dropout durante o treino.',64,597,1120,42,25,teal);

s=slide('Treinamento e escolha','Reynato Junior | 1 minuto',
  'Explicar época, lote, perda e parada antecipada. A saída softmax e a perda com rótulos inteiros aparecem na aula 3; a parada antecipada, na aula 5.');
txt(s,'Lote: 32 imagens\nLimite: 80 épocas\nUma época: todo o treino',64,165,530,190,31);
txt(s,'A perda mede o erro.\nA validação ajuda a decidir\nquando parar.',680,165,520,190,31);
txt(s,'Escolhemos a rede pela acurácia na validação.',64,422,1130,75,34,navy,true);
txt(s,'O teste ficou reservado para depois da escolha.',64,548,1130,56,29,teal);

s=slide('Comparação na validação','Wallace Jardim | 1 minuto e 30 segundos',
  'Acurácia é porcentagem de acertos. O Dropout desliga temporariamente saídas durante o treino. Fonte: aula 5 e resultados da validação no notebook do projeto.');
table(s,[['Modelo','Acertos','Acurácia'],
  ['Referência: sempre 0','6 de 217','2,76%'],
  ['Rede com camadas densas','155 de 217','71,43%'],
  ['Rede convolucional inicial','160 de 217','73,73%'],
  ['Rede com Dropout','168 de 217','77,42%']],
  64,160,1152,385,[650,250,252]);
txt(s,'Dropout: oito acertos a mais nesta execução.',64,571,1110,65,29,teal,true);

s=slide('Perda durante o treinamento','Wallace Jardim | 1 minuto e 30 segundos',
  'Comparar treino e validação. A rede inicial recuperou a época 10; a rede com Dropout, a 29. A perda de treino cai depois que a validação deixa de melhorar, sinal de sobreajuste. Fonte: aulas 3 e 5 e históricos do notebook do projeto.');
await picture(s,'curvas.png',70,151,1135,380);
txt(s,'MLP (perceptron de múltiplas camadas); CNN (rede neural convolucional).',
  64,534,1120,35,20,gray);
txt(s,'A perda de treino caiu. A validação parou de melhorar.\nIsso indica sobreajuste; o Dropout ajudou nesta execução.',
  64,575,1140,73,27,navy);

s=slide('Resultado no teste final','Daniel Gil | 2 minutos',
  'A rede foi escolhida antes do teste. Fonte: notebook do projeto; Modelo de Relatório, seção 3.');
table(s,[['Modelo','Acertos','Acurácia'],
  ['Referência: sempre 0','6 de 216','2,78%'],
  ['Rede escolhida','178 de 216','82,41%']],
  64,158,1152,205,[650,250,252]);
await picture(s,'acertos_erros.png',64,380,762,255);
txt(s,'38 erros\n\nO → 0: 4 vezes\nS → 5: 2 vezes',850,404,350,210,28,navy);

s=slide('Limites e uso possível','Daniel Gil | 1 minuto',
  'O modelo pode demonstrar a classificação de um caractere isolado. Há imagens iguais com rótulos 0 e O. Não foi testado em outras imagens. Fonte: relatório, seções 5 e 6; Modelo de Relatório.');
txt(s,'Demonstração com um caractere isolado.',64,164,1130,68,37,teal,true);
txt(s,'As mesmas imagens podem ser chamadas de 0 ou O.\nHá somente seis exemplos por classe no teste.\nNão testamos fotos, placas ou documentos reais.',
  64,294,1140,210,31);
txt(s,'Uma pessoa deve conferir cada sugestão do modelo.',64,550,1120,65,29,navy,true);

for(const [i,slideItem] of P.slides.items.entries()){
  const png=await P.export({slide:slideItem,format:'png',scale:1});
  await fs.writeFile(path.join(build,`slide-${String(i+1).padStart(2,'0')}.png`),
    new Uint8Array(await png.arrayBuffer()));
}
const candidate=path.join(build,'candidate.pptx');
await (await PresentationFile.exportPptx(P)).save(candidate);
const finalDir=path.join(build,'final');
await fs.mkdir(finalDir,{recursive:true});
const finalized=path.join(finalDir,`Apresentacao_${Date.now()}.pptx`);
await finalizePresentation({
  workspaceDir:root,candidatePath:candidate,finalPath:finalized,
  pythonExecutable:'C:/Users/danie/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
  integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit',
    ...[4,5,7,9].flatMap(n=>['--require-native-table-slide',String(n)])],
  requiredNativeTableOwnerSlides:[4,5,7,9],
  fontPolicy:{basis:'design',families:['Arial']},
  verifyArtifactToolImport:true,
  receiptPath:path.join(build,path.basename(finalized)+'.validation.json')
});
await fs.copyFile(finalized,path.join(root,'Apresentacao_Grupo4.pptx'));
console.log('Apresentação criada.');
