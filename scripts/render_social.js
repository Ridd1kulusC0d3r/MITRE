// render_social.js — converte assets/social.svg (gerado) em assets/social.png, 1280×640,
// usado como pré-visualização social do repositório (o GitHub não aceita SVG nesse campo).
// Requer Playwright com Chromium:  node scripts/render_social.js
// Depois: Settings → General → Social preview → enviar assets/social.png.
const path = require("path");
const { chromium } = require("playwright");
(async () => {
  const root = path.resolve(__dirname, "..");
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 640 }, deviceScaleFactor: 1 });
  await page.goto("file://" + path.join(root, "assets", "social.svg"));
  await page.screenshot({ path: path.join(root, "assets", "social.png") });
  await browser.close();
  console.log("assets/social.png gravado");
})();
