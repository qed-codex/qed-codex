---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsLineBundleOfThickenings.lean",
  "declarations": [
    "GlobalTheory.LBAlgLocal.exists_lineBundle_of_thickenings"
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

## Algebraization of line bundles on compatible thickenings

[Theorem AG.0693](https://andrewodesky.com/rh/lean/GlobalTheory.LBAlgLocal.exists_lineBundle_of_thickenings/)

Let $R$ be a commutative Noetherian local ring, $I\ne R$ an ideal, and assume $R$ is separated and complete for the $I$-adic topology. Let $B$ be a flat projective $R$-scheme. For each $e\ge0$, let $Y_e$ be an $R/I^{e+1}$-scheme, with maps $\beta_e:Y_e\to Y_{e+1}$ and $b_e:Y_e\to B$. Assume both squares $$\begin{matrix} Y_e&\xrightarrow{\beta_e}&Y_{e+1}\\ \downarrow&&\downarrow\\ \operatorname{Spec}(R/I^{e+1})&\longrightarrow&\operatorname{Spec}(R/I^{e+2}) \end{matrix} \qquad \begin{matrix} Y_e&\xrightarrow{b_e}&B\\ \downarrow&&\downarrow\\ \operatorname{Spec}(R/I^{e+1})&\longrightarrow&\operatorname{Spec}R \end{matrix}$$ are Cartesian and $b_{e+1}\beta_e=b_e$. For line bundles $N_e$ on $Y_e$, suppose given line-bundle isomorphisms $N_e\simeq\beta_e^*N_{e+1}$. Then there is a line bundle $M$ on $B$ with $N_e\simeq b_e^*M$ for every $e$.
