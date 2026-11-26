---
{
  "module": "Paper/Curvature.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Curvature.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Curvature.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Prices are nonpositively curved"

The subsection "Means" is in Paper/Means.lean, Theorem thm:cn and its proof are in Paper/Fan.lean, the definition of CAT(0)
spaces and Lemma lem:toolkit in Paper/Toolkit.lean; this file has Proposition prop:space.


### `prop_space_step`

 One step of the proof of Proposition prop:space: "let V_{l+1} be V_l with a new point for each pair of its points; define
prices by placing each new point at either end with probability ½ (Proposition prop:random)." The points are named by terms;
V_n consists of the terms of depth at most n. 

### `prop_space_midpoints`

 "Each step extends the one before, so together they form a price; in it each new point is a midpoint of its pair". 

### `prop_space_cauchy`

 "Midpoints of Cauchy sequences are Cauchy by (CN) itself": if a n → x and b n → v, and m n satisfies (CN) for a n and b n,
then (m n) is a Cauchy sequence. 

### `prop_space_completion`

 "The completion satisfies (CN)": a complete metric space is CAT(0) if any two points x, v of a dense subset S have a
point m for which (CN) holds at all z in S. 

### `prop_space_limit`

 "Its metric is a price as a limit": if the distance of a pseudometric space is a price, so is the metric of its
completion. 

### `prop_space`

 **Paper: Proposition prop:space.** "Every price on a set V is the pull-back of the metric of a price space." A price
space is a complete CAT(0) space whose metric is a price. 
