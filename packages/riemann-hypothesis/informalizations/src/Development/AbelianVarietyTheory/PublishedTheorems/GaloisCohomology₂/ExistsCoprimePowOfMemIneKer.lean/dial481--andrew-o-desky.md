---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/ExistsCoprimePowOfMemIneKer.lean",
  "declarations": [
    "GlobalTheory.TameQuot.exists_isInvariantMap"
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

## A Frobenius normalization of the local invariant map

[Theorem GC.1477](https://andrewodesky.com/rh/lean/GlobalTheory.TameQuot.exists_isInvariantMap/)

Assume ([Local Tate duality](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)). Let $F$ be a number field with algebraic closure $\Omega$, let $v$ be a finite place with residue size $q$, and choose a valuation ring of $\Omega$ over $v$ with decomposition group $D_v$ and inertia group $I_v$. Let $\ell$ be prime, $n\ge0$, $\ell\nmid v$, $q\equiv1\pmod{\ell^n}$, and let $\zeta\in\Omega$ be a primitive $\ell^n$th root of unity. There is a $\mathbb Z/\ell^n\mathbb Z$-linear isomorphism $$\operatorname{inv}_v:H^2(D_v,\mathbb Z/\ell^n\mathbb Z(1))\xrightarrow{\sim}\mathbb Z/\ell^n\mathbb Z$$ with the following normalization. For every $x\in\Omega$ with $x^{\ell^n}=\varpi$, where $\varpi\in\mathcal O_F$ has valuation one at $v$, every cyclotomic cocycle $\kappa$ with $g(x)=\zeta^{\kappa(g)}x$, every trivial-action cocycle $\chi$ vanishing on $I_v$, and every arithmetic Frobenius lift $\phi\in D_v$, $$\operatorname{inv}_v([\chi]\smile[\kappa])=\chi(\phi).$$
