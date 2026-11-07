import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import vm from "node:vm";

const source = fs.readFileSync(new URL("../assets/js/site.js", import.meta.url), "utf8");

function classList() {
  const names = new Set();
  return {
    toggle(name, on) {
      if (on) names.add(name);
      else names.delete(name);
    },
    has(name) {
      return names.has(name);
    },
  };
}

test("research filter hides engineering cards", () => {
  const cards = [
    { dataset: { category: "research" }, hidden: false },
    { dataset: { category: "engineering" }, hidden: false },
    { dataset: { category: "research" }, hidden: false },
  ];
  const buttons = ["all", "research", "engineering"].map((filter) => ({
    dataset: { filter },
    classList: classList(),
    attrs: {},
    setAttribute(name, value) {
      this.attrs[name] = value;
    },
    addEventListener(type, fn) {
      this.listeners = { [type]: fn };
    },
  }));
  const status = { textContent: "" };
  const document = {
    querySelectorAll(selector) {
      if (selector === "[data-filter]") return buttons;
      if (selector === "[data-category]") return cards;
      return [];
    },
    querySelector() {
      return null;
    },
    getElementById(id) {
      return id === "filter-status" ? status : null;
    },
  };
  const context = { document, matchMedia: () => ({ matches: true }) };
  vm.createContext(context);
  vm.runInContext(source, context);
  buttons[1].listeners.click();
  assert.equal(cards[0].hidden, false);
  assert.equal(cards[1].hidden, true);
  assert.equal(cards[2].hidden, false);
  assert.equal(status.textContent, "Showing 2 projects");
  assert.equal(buttons[1].classList.has("active"), true);
  assert.equal(buttons[0].classList.has("active"), false);
  assert.equal(buttons[1].attrs["aria-pressed"], "true");
});
