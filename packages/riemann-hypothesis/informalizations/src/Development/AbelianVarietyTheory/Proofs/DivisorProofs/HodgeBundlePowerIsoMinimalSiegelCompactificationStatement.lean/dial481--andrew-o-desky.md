---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HodgeBundlePowerIsoMinimalSiegelCompactificationStatement.lean",
  "declarations": [
    "GlobalTheory.T.hodgeBundle_power_iso_minimalSiegelCompactification"
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

## Commensurable powers of the Hodge and compactification line bundles

[Theorem AV.1544](https://andrewodesky.com/rh/lean/GlobalTheory.T.hodgeBundle_power_iso_minimalSiegelCompactification/)

Let $g,n\ge0$ and let $\mathcal X$ be the source's Siegel moduli family of dimension $g$ and level $n$ over its cyclotomic coefficient ring $R_n$, with universal abelian scheme $A$. Let $i:\mathcal X\to Z$ be a dense open immersion over $R_n$, where $Z$ is normal, Noetherian and projective, and let $L_Z$ be ample. Assume the full minimal-compactification package: the specified integral theta-divisor condition holds; there are a finite injective coefficient extension $R_n\to R'$, a normal projective $R'$-scheme $S'$, a proper surjection $\pi':S'\to Z$ compatible with the coefficient maps, a dense open $U'\subseteq S'$, and a finite surjection $c:U'\to\mathcal X$ with $\pi'|_{U'}=i\circ c$. There is a commutative semiabelian scheme $G'/S'$ smooth of relative dimension $g$, extending $c^*A$, and some $N'\ge1$ with $$\pi'^*L_Z\simeq\bigl(\det e_{G'}^*\Omega^1_{G'/S'}\bigr)^{\otimes N'}.$$

Let $\pi:S\to Z$ have $S$ normal and $S\to\operatorname{Spec}R_n$ projective. Suppose $j:\mathcal X\hookrightarrow S$ has dense image and $\pi\circ j=i$. Let $G/S$ be semiabelian, smooth of relative dimension $g$, with a specified group pullback identification $j^*G\simeq A$. Then there are integers $a,N\ge1$ such that $$\bigl(\det e_G^*\Omega^1_{G/S}\bigr)^{\otimes N}\simeq(\pi^*L_Z)^{\otimes a}.$$
