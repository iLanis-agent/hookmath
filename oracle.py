import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def row_plan(railCm, pitchCm):
    if not (railCm > 0) or not (pitchCm > 0):
        return {"error": "the rail length and the labeled pitch must be positive"}
    hooks = math.floor(railCm / pitchCm)
    if hooks < 1:
        return {"error": "the rail is shorter than one labeled hook pitch"}
    leftover = round1(railCm - hooks * pitchCm)
    if hooks <= 3: verdict = "a short rail"
    elif hooks <= 6: verdict = "a family rail"
    else: verdict = "a long rail"
    return {"hooks": hooks, "leftover": leftover, "verdict": verdict}

def line_plan(tallestCm, factorPct):
    if not (tallestCm > 0):
        return {"error": "the height must be positive"}
    if not (factorPct > 0):
        return {"error": "the labeled factor must be positive"}
    line = round1(tallestCm * factorPct / 100)
    if line < 150: verdict = "a low line"
    elif line < 175: verdict = "a standard line"
    else: verdict = "a high line"
    return {"line": line, "verdict": verdict}

def depth_plan(spaceCm, projectionCm):
    if not (spaceCm > 0) or not (projectionCm > 0):
        return {"error": "the space and the labeled projection must be positive"}
    margin = round1(spaceCm - projectionCm)
    if margin >= 5: verdict = "clears with room to hang"
    elif margin >= 0: verdict = "clears, just"
    else: verdict = "sticks out past the space"
    return {"margin": margin, "verdict": verdict}

def render_row(r, railCm, pitchCm):
    return ("A rail " + fmt(railCm) + " cm long at a labeled " + fmt(pitchCm) + " cm a hook fits "
            + plural(r["hooks"], "hook") + " with " + fmt(r["leftover"]) + " cm to spare - " + r["verdict"] + ".")

def render_line(r, tallestCm, factorPct):
    return ("The tallest hanger at " + fmt(tallestCm) + " cm puts the hook line near " + fmt(r["line"])
            + " cm at a labeled " + fmt(factorPct) + "% of height - " + r["verdict"] + ".")

def render_depth(r, spaceCm, projectionCm):
    return ("Hooks projecting a labeled " + fmt(projectionCm) + " cm into " + fmt(spaceCm) + " cm of space leave a margin of "
            + fmt(r["margin"]) + " cm - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[60,15],[90,15],[45,15],[120,15],[10,15],[0,15],[60,0],[100,15],[62.5,15],[75,18]]:
    add("rowPlan", row_plan, render_row, a)
for a in [[160,105],[180,105],[140,105],[200,105],[167.5,105],[0,105],[160,0],[160,100],[175,105],[150,110]]:
    add("linePlan", line_plan, render_line, a)
for a in [[20,12],[15,12],[10,12],[17,12],[0,12],[20,0],[12.5,12],[30,12],[8,12],[20,20]]:
    add("depthPlan", depth_plan, render_depth, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
