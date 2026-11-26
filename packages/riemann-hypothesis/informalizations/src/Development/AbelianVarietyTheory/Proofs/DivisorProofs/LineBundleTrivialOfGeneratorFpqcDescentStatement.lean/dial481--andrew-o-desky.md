---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LineBundleTrivialOfGeneratorFpqcDescentStatement.lean",
  "declarations": [
    "GlobalTheory.T.lineBundle_trivial_of_generator_fpqc_descent"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Triviality from a compatible generator on an fpqc cover

[Theorem AG.1091](https://andrewodesky.com/rh/lean/GlobalTheory.T.lineBundle_trivial_of_generator_fpqc_descent/)

Let $M$ be a line bundle on a scheme $X$, and let $f:X'\to X$ be flat, surjective and quasi-compact. Let $Z$ with maps $g_1,g_2:Z\to X'$ be a fibre product $X'\times_X X'$. If $f^*M$ has a nowhere-vanishing global section $t$ whose two pullbacks to $Z$ agree under the canonical identification $g_1^*f^*M\simeq g_2^*f^*M$, then $M$ is trivial.
