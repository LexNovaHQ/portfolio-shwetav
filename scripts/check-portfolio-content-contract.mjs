import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const read = (p) => fs.readFileSync(path.join(root, p), "utf8");
const canonical = JSON.parse(read("content.json"));
const proof = canonical.registry_proof;
const headline = "A litigator making AI legal work defensible enough to deploy.";
const doctrine = "Model suggests. Rules decide. Evidence locks. Conflicts block auto-lock.";
const lineage = "Registry lineage: 81 → 98 AI-governance rows. A second FinTech registry now contains 46 routable rows under the same key structure.";

assert.ok(proof, "content.json registry_proof missing");
assert.equal(proof.ai_governance.routable_rows, 98);
assert.equal(proof.ai_governance.key_version, "v4.0");
assert.equal(proof.fintech.routable_rows, 46);
assert.equal(proof.fintech.key_version, "v1.0");
assert.equal(proof.fintech.built_to_structure_of, "AI_Registry_Key.yml");
assert.equal(proof.doctrine, doctrine);
assert.equal(proof.lineage, lineage);
assert.deepEqual(proof.derivation_order, ["Behavior Class","Lane","Surface","Subcategory / Terminal Harm","Compliance Framework","Severity","Threat Trigger"]);
assert.deepEqual(proof.sample_rows.map((r) => r.threat_id), ["PAY_LIC_001","XCHG_LIC_001","SCOR_CONS_001"]);
assert.equal(canonical.hero.headline, headline);
assert.match(canonical._meta.og_title, /Technology & Data Protection Lawyer/);

const pages = ["index.html","legal-grammar.html","applied-legal-architecture.html","legal-architecture-in-operation.html"];
for (const file of pages) {
  const source = read(file);
  const match = source.match(/<script id="content-data" type="application\/json">([\s\S]*?)<\/script>/);
  assert.ok(match, `${file}: embedded content-data missing`);
  const embedded = JSON.parse(match[1]);
  assert.deepEqual(embedded, canonical, `${file}: embedded content drift`);
  assert.ok(source.includes(headline), `${file}: canonical headline absent`);
  assert.ok(source.includes(doctrine), `${file}: doctrine absent`);
}

const grammar = read("legal-grammar.html");
assert.ok(grammar.includes('id="registry-transfer"'), "Act I registry-transfer anchor missing");
assert.ok(grammar.includes("Two registries. One key structure."), "Act I registry title missing");
assert.ok(grammar.includes("built_to_structure_of"), "Act I structural proof missing");
const operation = read("legal-architecture-in-operation.html");
assert.ok(operation.includes('id="operating-doctrine"'), "Act III operating-doctrine anchor missing");
assert.ok(read("assets/editorial-multipage.js").includes("['Registry Transfer','registry-transfer']"), "Act I rail item missing");
assert.ok(read("assets/editorial-multipage-fixes.css").includes(".registry-transfer"), "registry transfer styles missing");

const forbidden = [
  ["80", "-point"].join(""),
  ["80", " point"].join(""),
  ["refined", " from 81"].join(""),
  ["Shwet", "av Singh"].join(""),
  ["shwetav", ".alpna.singh@gmail.com"].join("")
];
const deadLabels = ["Watch walkthrough","Watch prompt-agent walkthrough","View scrubbed output sample","View automation build notes","Watch Category 2 demo"];
const textExtensions = new Set([".html",".json",".js",".css",".md",".txt",".yml",".yaml"]);
const skip = new Set([path.normalize("scripts/check-portfolio-content-contract.mjs")]);
const escapeRegExp = (value) => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if ([".git","node_modules"].includes(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (textExtensions.has(path.extname(entry.name)) && !skip.has(path.relative(root, full))) {
      const text = fs.readFileSync(full, "utf8");
      for (const token of forbidden) assert.ok(!text.includes(token), `${path.relative(root, full)}: forbidden stale token ${token}`);
      for (const label of deadLabels) assert.ok(!new RegExp(`href=["']#["'][^>]*>\\s*${escapeRegExp(label)}`, "is").test(text), `${path.relative(root, full)}: dead CTA ${label}`);
    }
  }
}
walk(root);
console.log(JSON.stringify({check:"portfolio content contract",status:"PASS",pages:pages.length,ai_rows:98,fintech_rows:46}, null, 2));
