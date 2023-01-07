---
link: 
  - rel: "stylesheet"
    href: "css/sample5-inlineSVG.css"
---

［挿入］<span class="imarker">1</span>→［図］<span class="imarker">2</span>→［画像］<span class="imarker">3</span>→［このデバイス］<span class="imarker">4</span>の順にクリックします。

<figure>
  <svg width="442" height="200">
    <defs>
      <path d="M0,0 L15,0 L20,10 L15,20, L0,20 L0,0" stroke="#fff" fill="#f00" id="marker"/>
    </defs>
    <image href="img/img7-excel.png" transform="scale(0.4)"/>
    <rect width="442" height="200" stroke="#000" fill="transparent" stroke-width="1"/>
    <use href="#marker" x="40" y="20"/><text x="40" y="20">1</text>
    <use href="#marker" x="83" y="60"/><text x="83" y="60">2</text>
    <use href="#marker" x="86" y="100"/><text x="86" y="100">3</text>
    <use href="#marker" x="88" y="140"/><text x="88" y="140">4</text>
  </svg>
</figure>
