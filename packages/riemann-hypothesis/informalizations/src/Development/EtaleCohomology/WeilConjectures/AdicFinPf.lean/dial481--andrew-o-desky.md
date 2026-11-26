---
{
  "module": "src/Development/EtaleCohomology/WeilConjectures/AdicFinPf.lean",
  "declarations": [
    "LateralTheory.EWeil.AdicFinPf.AdicFin_of"
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

## Finite generation of an adic cohomology limit

[Theorem PHT.1274](https://andrewodesky.com/rh/lean/LateralTheory.EWeil.AdicFinPf.AdicFin_of/)

Let $\ell$ be prime and let $X$ be a simplicial presheaf on the category of schemes, using the cohomology construction in ([Mayer–Vietoris for simplicial presheaves on the etale site](https://andrewodesky.com/rh/lean/GlobalTheory.EtC.mayerVietoris/)). Fix integers $n,i$, and put $$H_k=H^n(X,\mathbb Z/\ell^k\mathbb Z(i)),\qquad H=\varprojlim_{k\ge0}H_k,$$ with the prescribed coefficient-reduction transition maps and projections $p_k:H\to H_k$. Assume that every $H_k$ is finite and that $$p_k(x)=0\Longrightarrow x=\ell^k y\text{ for some }y\in H\qquad(k\ge0,\ x\in H).$$ Then $H$ is a finitely generated $\mathbb Z_\ell$-module.
