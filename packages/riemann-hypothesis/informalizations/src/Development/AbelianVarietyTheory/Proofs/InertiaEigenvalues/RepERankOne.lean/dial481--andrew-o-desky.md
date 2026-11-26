---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RepERankOne.lean",
  "declarations": [
    "GlobalTheory.TwistAbove.twist_above"
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

## Period properties and filtration jumps after a rank-one twist

[Theorem PHT.1355](https://andrewodesky.com/rh/lean/GlobalTheory.TwistAbove.twist_above/)

Let $\ell$ be prime and fix local period-ring and integral data as in ([An invariant crystalline period matrix for an unramified representation](https://andrewodesky.com/rh/lean/GlobalTheory.UnrPer.exists_period_unramified/)). Let $E$ be a number field, $\Omega$ a field over $E$, and $\Gamma\subseteq\operatorname{Aut}_E(\Omega)$ a subgroup. Fix a commutative topological $\mathbb Z_\ell$-algebra $\mathcal O$ and a local comparison bridge from $\Gamma$ to the local Galois and period data, with the bridge conditions of ([A de Rham character preserves the de Rham condition under twisting](https://andrewodesky.com/rh/lean/GlobalTheory.T.deRham_characterTwist_iff_localEmbedding/)). Let $$r,r':\Gamma\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell),\qquad \mu:\Gamma\to\overline{\mathbb Q}_\ell^{\times},\qquad r'(g)=\mu(g)r(g).$$ If $r$ and the rank-one representation $\mu$ are de Rham at this bridge, then $r'$ is de Rham there; the same implication holds for crystalline representations and for potentially crystalline representations.

For every embedding $\tau:E\to\overline{\mathbb Q}_\ell$, every multiset $J$ of integers and $c\in\mathbb Z$, if the filtration-jump conditions for the chosen local bridge hold for $r$ with multiset $J$ and for $\mu$ with singleton multiset $\{c\}$, they hold for $r'$ with multiset $$\{j+c:j\in J\},$$ with multiplicities retained.
