---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/PatchOne.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Core.patchOne_holds"
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

## Quadratic CM patching using primes of prime absolute norm

[Theorem AGR.0162](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Core.patchOne_holds/)

Let $F$ be a number field, $\Omega$ an algebraic closure of $F$, $\ell$ a prime, $a$ a nonnegative integer, and $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$ a field isomorphism. For every finite prime $v$ of $F$, let $\mathcal S_v$ be a relation on finite multisets in $\mathbb C^\times$, with at most one multiset satisfying $\mathcal S_v$.

Let $\mathcal K$ be an infinite set of quadratic intermediate fields $F\subset K\subset\Omega$, each a CM field. For each $K\in\mathcal K$, let $$r_K:G_K\longrightarrow\mathrm{GL}_a(\overline{\mathbb Q}_\ell)$$ be continuous and semisimple, where $G_K=\operatorname{Gal}(\Omega/K)$. Assume that for each $K$, at all but finitely many finite primes $w$ of $K$ whose absolute norm $q_w$ is a rational prime, there is a multiset $B$ with $\mathcal S_{w|_F}(B)$ such that $r_K$ is unramified at $w$ and $$\iota\bigl(\det(T-r_K(\operatorname{Frob}_w^{-1}))\bigr)=\prod_{\beta\in B}(T-q_w^{(a-1)/2}\beta).$$ Then there is a continuous semisimple representation $$\rho:G_F\longrightarrow\mathrm{GL}_a(\overline{\mathbb Q}_\ell),\qquad G_F=\operatorname{Gal}(\Omega/F),$$ such that $r_K\simeq\rho|_{G_K}$ for all but finitely many $K\in\mathcal K$.

The conclusion also holds if the local compatibility assumption is replaced by the following one. For each $K\in\mathcal K$, at all but finitely many finite primes $w$ of $K$, put $v=w|_F$, $q_v=\#(\mathcal O_F/v)$ and $q_w=\#(\mathcal O_K/w)$. For every nonnegative integer $f$ with $q_w=q_v^f$, there is a multiset $B$ with $\mathcal S_v(B)$ such that $r_K$ is unramified at $w$ and $$\iota\bigl(\det(T-r_K(\operatorname{Frob}_w^{-1}))\bigr)=\prod_{\beta\in B}\bigl(T-(q_v^{(a-1)/2}\beta)^f\bigr).$$
