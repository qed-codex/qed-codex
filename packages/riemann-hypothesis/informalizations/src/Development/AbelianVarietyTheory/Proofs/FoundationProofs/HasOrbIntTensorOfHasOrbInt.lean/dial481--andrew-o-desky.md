---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/HasOrbIntTensorOfHasOrbInt.lean",
  "declarations": [
    "GlobalTheory.Orb.hasOrbInt_tensor"
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

## Product formula for a pure-tensor orbital integral

[Theorem REP.0499](https://andrewodesky.com/rh/lean/GlobalTheory.Orb.hasOrbInt_tensor/)

Let $F,E$ be number fields with $E$ an $F$-algebra, let $\sigma\in\operatorname{End}_{F\text{-alg}}(E)$, and let $J\in M_n(E)$. Put $$G(R)=\{g\in\operatorname{GL}_n(E\otimes_FR):(\sigma\otimes1)(g)^tJg=J\}.$$ Let $L\subset E^n$ be a full $\mathcal O_E$-lattice and $K_v\subset G(F_v)$ its stabilizer. Fix $\gamma\in G(\mathbb A_F)$, with components $\gamma_v$ and local centralizers $C_v$. Choose product Haar measures on $G(\mathbb A_F)$ and $C_{G(\mathbb A_F)}(\gamma)$ as specified below, with every local centralizer measure right-invariant. Let $f_v$ be continuous and compactly supported at infinite places and locally constant and compactly supported at finite places, with $f_v=\mathbf1_{K_v}$ for almost all finite $v$.

Assume that for almost all finite $v$, $$\{x\in G(F_v):x^{-1}\gamma_vx\in K_v\}=C_vK_v.$$ At each place assume either that the local conjugation orbit is proper modulo $C_v$, or that the local orbital integral exists absolutely. Then every local orbital integral exists absolutely, almost all finite local factors equal one, the global centralizer measure is right-invariant, and $$O_\gamma\left(\bigotimes_v f_v\right)=\prod_{v\mid\infty}O_{\gamma_v}(f_v)\prod_{v\nmid\infty}O_{\gamma_v}(f_v).$$ The global orbital integral also exists absolutely.
