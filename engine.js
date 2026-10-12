(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function rowPlan(railCm, pitchCm) {
    if (!(railCm > 0) || !(pitchCm > 0)) return { error: "the rail length and the labeled pitch must be positive" };
    var hooks = Math.floor(railCm / pitchCm);
    if (hooks < 1) return { error: "the rail is shorter than one labeled hook pitch" };
    var leftover = round1(railCm - hooks * pitchCm);
    var verdict;
    if (hooks <= 3) verdict = "a short rail";
    else if (hooks <= 6) verdict = "a family rail";
    else verdict = "a long rail";
    return { hooks: hooks, leftover: leftover, verdict: verdict };
  }

  function linePlan(tallestCm, factorPct) {
    if (!(tallestCm > 0)) return { error: "the height must be positive" };
    if (!(factorPct > 0)) return { error: "the labeled factor must be positive" };
    var line = round1(tallestCm * factorPct / 100);
    var verdict;
    if (line < 150) verdict = "a low line";
    else if (line < 175) verdict = "a standard line";
    else verdict = "a high line";
    return { line: line, verdict: verdict };
  }

  function depthPlan(spaceCm, projectionCm) {
    if (!(spaceCm > 0) || !(projectionCm > 0)) return { error: "the space and the labeled projection must be positive" };
    var margin = round1(spaceCm - projectionCm);
    var verdict;
    if (margin >= 5) verdict = "clears with room to hang";
    else if (margin >= 0) verdict = "clears, just";
    else verdict = "sticks out past the space";
    return { margin: margin, verdict: verdict };
  }

  function renderRow(r, railCm, pitchCm) {
    return "A rail " + railCm + " cm long at a labeled " + pitchCm + " cm a hook fits " + plural(r.hooks, "hook") + " with " + r.leftover + " cm to spare - " + r.verdict + ".";
  }

  function renderLine(r, tallestCm, factorPct) {
    return "The tallest hanger at " + tallestCm + " cm puts the hook line near " + r.line + " cm at a labeled " + factorPct + "% of height - " + r.verdict + ".";
  }

  function renderDepth(r, spaceCm, projectionCm) {
    return "Hooks projecting a labeled " + projectionCm + " cm into " + spaceCm + " cm of space leave a margin of " + r.margin + " cm - " + r.verdict + ".";
  }

  var api = { rowPlan: rowPlan, linePlan: linePlan, depthPlan: depthPlan, renderRow: renderRow, renderLine: renderLine, renderDepth: renderDepth };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.HookMath = api;
})(this);
