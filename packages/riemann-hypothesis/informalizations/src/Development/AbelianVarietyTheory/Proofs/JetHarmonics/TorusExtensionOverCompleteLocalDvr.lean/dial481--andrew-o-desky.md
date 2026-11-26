---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/TorusExtensionOverCompleteLocalDvr.lean",
  "declarations": [
    "GlobalTheory.TorusModel.isAdicColimit_of_finite_flat"
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

## Maps from a finite flat algebra are determined by its thickenings

[Theorem AG.0804](https://andrewodesky.com/rh/lean/GlobalTheory.TorusModel.isAdicColimit_of_finite_flat/)

Let $R$ and $O$ be commutative rings, let $O$ be local with maximal ideal $\mathfrak m$, let $I\subset R$ be an ideal, and let $u:R\to O$ be a ring homomorphism. Put $J=IO$. Assume $O$ is $J$-adically complete and every $a\in\mathfrak m$ has a power in $J$. Let $A$ be a finite flat $O$-algebra and put $$T=\operatorname{Spec}A,\qquad T_e=\operatorname{Spec}(A/I^{e+1}A)\quad(e\ge0).$$ For every scheme $X$ and compatible family of morphisms $f_e:T_e\to X$, there is a unique morphism $f:T\to X$ restricting to $f_e$ for every $e$.
