---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsLbOfGeneratedSystem.lean",
  "declarations": [
    "GlobalTheory.GenSystem.exists_lb_of_generated_system"
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

## Algebraization of a generated system of line bundles

[Theorem AG.1093](https://andrewodesky.com/rh/lean/GlobalTheory.GenSystem.exists_lb_of_generated_system/)

Let $R$ be a noetherian local commutative ring, complete and separated for a proper ideal $I$. Set $S_e=\operatorname{Spec}(R/I^{e+1})$. Let $Y_e/S_e$ be schemes with transition maps $\beta_e:Y_e\to Y_{e+1}$ identifying $Y_e$ with $Y_{e+1}\times_{S_{e+1}}S_e$. Let $B/R$ be flat and projective with maps $b_e:Y_e\to B$ identifying $Y_e$ with $B\times_R S_e$ and satisfying $b_{e+1}\beta_e=b_e$.

Let $H_e$ be line bundles on $Y_e$ with isomorphisms $v_e:H_e\simeq\beta_e^*H_{e+1}$. Suppose there are sections $s_{e,0},\ldots,s_{e,n}$, for some $n\ge0$, compatible under $v_e$ and pullback, whose nonvanishing loci cover $Y_0$ at $e=0$. There exists a line bundle $M$ on $B$ with $H_e\simeq b_e^*M$ for every $e$.
