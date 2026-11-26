---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UniformLiftingOfSections.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.FormalAlg.Lift.exists_uniform_lift"
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

## Uniform lifting of sections through formal thickenings

[Theorem AG.0098](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.FormalAlg.Lift.exists_uniform_lift/)

Let $R$ be a noetherian commutative ring, $I\subset R$ an ideal, and $Y_e$ a proper scheme over $R/I^{e+1}$ for each $e\ge0$. Suppose maps $\beta_e:Y_e\to Y_{e+1}$ identify $Y_e$ with the base change of $Y_{e+1}$ to $R/I^{e+1}$. Let $N_e$ be line bundles with compatible isomorphisms $N_e\simeq\beta_e^*N_{e+1}$.

Let $d\ge1$ and suppose $m+1$ specified sections of $N_0^{\otimes d}$ give a relatively very ample embedding over $R/I$. There is $t_0\ge0$ such that, for every integer $t\ge t_0$ and every $e\ge0$, the restriction map $$H^0(Y_{e+1},N_{e+1}^{\otimes dt})\longrightarrow H^0(Y_e,N_e^{\otimes dt})$$ is surjective, using the given line-bundle isomorphisms.
