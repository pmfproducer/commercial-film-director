# Apple *1984* — registro de aquisição e resolução de versão

## Estado

`BROADCAST_RECORD_DERIVATIVE_RECODED_EXCERPT`; não é master de transmissão,
negativo, scan de filme, arquivo de pós-produção nem upload Apple validado. O
material permite leitura técnica instrumentada parcial, não equivalência ao
acabamento original. O nome local contém `broadcast_master` por legado de
aquisição e não é autoridade semântica.

## Cadeia de aquisição

1. O registro D&AD hospedado no Vimeo foi localizado e usado para créditos,
   mas o player recusou aquisição reproduzível com respostas `401/403`.
2. Foi localizado no Internet Archive o registro
   `BAVC1004566_SuperBowl8412284_prores`, integrante das coleções Marion Stokes
   TV Archive Experiment, News & Public Affairs e Marion Stokes Video.
3. O arquivo original catalogado é um QuickTime de `114276240951` bytes. Para
   viabilizar a busca temporal, usou-se o derivado público H.264 de
   `1584100722` bytes, MD5 `05bb6243dbc7821eb062ccf671c2ed6c` e SHA-1
   `9583319b5d6a5d628c93d18084293929471fd969`.
4. A localização do comercial foi feita por miniaturas de todo o registro,
   seguida de folhas a 1 s e checagem de bordas a 0,1 s. O recorte adotado
   começa em `02:45:41.200` e dura `60.100` s no derivado do broadcast.
5. O recorte foi recodificado em H.264/AAC para análise local. Portanto, seu
   hash identifica este objeto analítico, não o arquivo integral do Archive.

## Objeto analisado

- nome: `apple_1984_superbowl_broadcast_master.mp4`;
- SHA-256: `a294948a208e56b5005cd46c4b6887c5504751b793c0721e1c8d5ca21ed4b29c`;
- tamanho: `10773125` bytes;
- duração de contêiner: `60.126793` s;
- vídeo: H.264 High, `640×480`, 4:3, `2997/100` fps, progressivo, 1802 frames;
- áudio: AAC-LC, estéreo, 44,1 kHz, duração `60.100000` s;
- borda inicial: imagem do comercial, com estrutura industrial e número 14;
- borda final: preto após a marca; a chamada CBS seguinte não entra no recorte.

## Distinção de versões

- Este objeto é um recorte compatível com o trecho comercial de aproximadamente
  60 s dentro do registro do Super Bowl XVIII de 22 de janeiro de 1984; a
  equivalência a master ou cópia de preservação não foi demonstrada.
- O registro D&AD é outra transferência pública da peça, mas seu stream não foi
  adquirido; não se presume identidade de cor, áudio, enquadramento ou frames.
- O Paley cataloga uma peça de `0:01:00`, sem disponibilizar neste trabalho um
  master comparável.
- Há uma variante CGI de 2004 com iPod e fones adicionados digitalmente. É um nó
  separado, não adquirido, com créditos, direitos, intenção e acessibilidade
  próprios. Ela não completa este objeto: nas 241 amostras não aparecem esses
  elementos na figura ativa.

## Limites

- A janela foi resolvida em cópia de transmissão 4:3 comprimida e recodificada;
  overscan, crominância, ruído, contraste, dinâmica e mix podem divergir de
  outros masters.
- A amostragem temporal não prova fluidez de movimento nem elimina a
  possibilidade de eventos inferiores a 0,25 s.
- Nenhuma mídia foi declarada assistida ou ouvida. A evidência visual vem de
  folhas de contato; a sonora, de medições e ASR automático.
