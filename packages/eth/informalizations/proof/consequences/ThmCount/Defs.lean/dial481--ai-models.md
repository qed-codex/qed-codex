---
{
  "module": "proof/consequences/ThmCount/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix C: Theorem C from Theorem D(b), and the closing remark (definitions and statements only)

Theorem C: «One deterministic algorithm computes the number of satisfying assignments of a 3-CNF on
n ≥ 2 variables in time 2^{O(n/(log n)^{α/10})}», with α = 1/2. Its Lean sentence is
`PaperSentences.CountRate (1/20)`.
Here it is derived from Theorem D(b) (`MainTheoremForms.ThmVariablesB`: one algorithm, for all k ≥ 1
and n ≥ 4, time 2^{C·k²·n·log log n/√(log n)}) at k = 3.
THIS IS NOT THE ROUTE OF THE PRINTED SKETCH OF APPENDIX C, and this file does not make Lean's proof
of Theorem C «the paper's proof». It shows that Theorem C also follows from Theorem D(b) with k = 3.
There is no circle: Appendix D takes from Appendix C the changed sparsification procedure and
«exactly one output», not Theorem C.
Of the sketch, the sentences on the procedure are in
proof/sparsification/SparsificationLemma/Sketch.lean and «Φ has Z·2^{n−v} satisfying assignments» is
`Occ.StCountOcc` (proof/consequences/Occ/Defs.lean). Three steps have no statement anywhere: the
outputs are «produced in time 2^{εn} times a polynomial in n that does not depend on ε» (for the
thresholds taken to be Calabro's), «Theorem A(c) computes the number Z» at each output, and «The
time is bounded as in the proof of Theorem A(d), with M(ε)+2 in place of M(ε), and ε = (log
n)^{−α/10} gives the theorem».
Three things stand between the two sentences, and each is a named statement:
1. the input: the machine of D(b) reads 1ᵏ0 before the code; 2. the range: D(b) says nothing for n <
   4, Theorem C wants a machine that is right for every n and fast for n ≥ 2; so the front end adds
   four forced variables (`Wrap.pad4`), which keeps the number of satisfying assignments, and the
   last step takes the four highest bits off the output;
3. the rates: 9·(n+4)·log log(n+4)/√(log(n+4)) = O(n/(log n)^{1/20}) for n ≥ 2, also after the power
   q of the wrapper.
The statements `StFromVariablesB` and `StCanBeWrappedAndEveryWrapperCounts` are made for EVERY
machine with the body of D(b), so that they show the route.
This file has no theorem. 

### `MapsToPadded`

 The front end: the plain code of a 3-CNF φ is mapped to the code of (3, φ with four forced
variables more). Nothing is asked on other words. 

### `StFrontEnd`

 There is a polynomial-time front end. 

### `dropFour`

 The last step: the four highest bits are taken off. 

### `StPadKeepsCount`

 The four forced variables keep the number of satisfying assignments, and the number in n + 5
bits without its four highest bits is the number in n + 1 bits. 

### `StInputLength`

 The plain code of a 3-CNF on n variables has length polynomial in n. 

### `StRates`

 The comparison of the rates: for all constants C, q, a, d there is C' such that for every n ≥ 2,
q·(2^{C·9·(n+4)·log log(n+4)/√(log(n+4))} + a·(n+2)^d + 1)^q ≤ 2^{C'·n/(log n)^{1/20}}. 

### `StLastStep`

 The last step is polynomial-time. 

### `StFromVariablesB`

 **For EVERY machine M with the body of Theorem D(b)**, every front end as above (polynomial-time
or not) and every machine N that wraps M with it and with `dropFour`: N computes the number of
satisfying assignments of every 3-CNF, on n ≥ 2 variables in time 2^{C'·n/(log n)^{1/20}}. 

### `StCanBeWrappedAndEveryWrapperCounts`

 Existence and the statement on every wrapper in one: for EVERY machine M with finite alphabets
and the body of Theorem D(b), (1) there are a polynomial-time front end, a machine N with finite
alphabets and q such that N wraps M with it and with `dropFour`; (2) every such N counts, as in
`StFromVariablesB`. 

### `StTheorem`

 Theorem C from Theorem D(b). It follows, with the statements above, from
`StCanBeWrappedAndEveryWrapperCounts`. 

 ### The closing remark of Appendix C

«For clauses of 3 literals, a bound in Calabro's proof gives M(ε) = O(ε^{-2} log²(1/ε)), and with it
the time becomes 2^{O(n(log log n)^{2/3}/(log n)^{α/3})}.»
The first half is stated for the outputs of the procedure (`StMEpsClauses`). The second half is
stated only as a sentence that follows from Theorem D(b); the remark's own derivation of the time is
not stated. 

### `StMEps`

 The bound on the occurrences of a literal in the formula ψ at a leaf, at k = 3: 2 + 4α·(32α), α =
`SparsificationLemma.Cal.alphaC 3 ε`. (A leaf has at most 2n times this many clauses; for the
outputs themselves see `StMEpsClauses`.) It is O(ε^{-2}·log²(1/ε)) for 0 < ε ≤ 1/2 (the paper's O is
for ε → 0; near ε = 1 the logarithm vanishes). 

### `StMEpsClauses`

 «gives M(ε) = O(ε^{-2} log²(1/ε))», at k = 3, for the outputs themselves: every output of the
procedure of Appendix C with the thresholds taken to be Calabro's
(`SparsificationLemma.Cal.sparsify 3 n ε φ`) has at most (A·ε^{-2}·log²(1/ε) + 2)·n clauses, for 0 <
ε ≤ 1/2. 

### `StRemarkTime`

 The time of the remark, as a sentence (α = 1/2), for n ≥ 4: one deterministic algorithm computes
the number of satisfying assignments of a 3-CNF on n ≥ 4 variables in time 2^{O(n(log log
n)^{2/3}/(log n)^{1/6})}. It is weaker than Theorem D(b) at k = 3 and is derived from it by
comparing the rates, not by the route of the remark. 
