---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TensOfForallIsPsEff.lean",
  "declarations": [
    "GlobalTheory.IsAmpleLB.tens_of_forall_isPsEff"
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

## Ampleness after tensoring with a bundle positive on subvarieties

[Theorem AG.1157](https://andrewodesky.com/rh/lean/GlobalTheory.IsAmpleLB.tens_of_forall_isPsEff/)

Let $k$ be a field, $X\to\operatorname{Spec}k$ a projective scheme, $A$ an ample line bundle, and $N$ a line bundle on $X$. Suppose that for every irreducible closed subset $Z\subset X$, the restriction $N|_{Z_{\mathrm{red}}}$ is pseudo-effective in the following sense: there exists an ample line bundle $B$ on $Z_{\mathrm{red}}$ such that, for each integer $m\ge1$, some integer $r\ge1$ satisfies $$H^0\!\left(Z_{\mathrm{red}},((N|_{Z_{\mathrm{red}}})^{\otimes m}\otimes B)^{\otimes r}\right)\ne0.$$ Then $A\otimes N$ is ample.
