# Hook math

Hook math plans the coat rail before the drill: the rail length at a labeled
pitch becomes the hook count, the tallest hanger's height at a labeled factor
becomes the hook line, and the space minus a labeled hook projection becomes
the clearance margin.

Live site: https://ilanis-agent.github.io/hookmath/

## The three tools

- **Row plan** - `floor(rail / labeled pitch (15 cm))` hooks and the
  centimeters left over, with a short / family / long verdict.
- **Line plan** - `tallest height x labeled factor (105%)`, the hook line,
  with a low / standard / high verdict.
- **Depth plan** - `space - labeled projection (12 cm)`, the clearance
  margin, with a room / just / sticks-out verdict.

## Limits

Every default is labeled and illustrative. Walls, households and hooks all
vary. This is planning arithmetic, not a mounting instruction: measure the
real wall and follow the hook maker's fixing sheet.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 136 checks)

Run the tests: `python3 oracle.py && node test.js`
