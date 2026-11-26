---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/HyperbolicEntryBounds/ChainPlug.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.F.F0.complex_coefficient_multiplicity_holds"
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

## A finite geometric expansion for a unitary trace distribution

[Theorem AGR.1256](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.F.F0.complex_coefficient_multiplicity_holds/)

Let $E$ be a CM field unramified at every finite prime over its maximal real subfield $F$, and let $n\ge1$. Choose a unitary Hecke character $\mu$ of $E$ whose restriction to $\mathbb A_F^\times$ is the quadratic character of $E/F$, whose component at every nonsplit finite place is the unramified character taking a uniformizer to $-1$, and whose infinity type is $(z_v/|z_v|)^{e_v}$ with each $e_v$ odd. For each infinite place $v$ of $E$, choose a dominant integral weight $\lambda_v$ of rank $n$.

There are a finite index set $I$, integers $0\le a_i\le n$, dominant integral weights $\lambda_{1,i,v}$ of rank $a_i$ and $\lambda_{2,i,v}$ of rank $n-a_i$, and nonzero complex numbers $s_i$, such that $$\bigl(\mathcal I(\lambda_{1,i,v})+(n-a_i)e_v/2\bigr)\sqcup\bigl(\mathcal I(\lambda_{2,i,v})+a_i e_v/2\bigr)=\mathcal I(\lambda_v).$$ For a rank-$b$ weight $\alpha$, $\mathcal I(\alpha)=\{\alpha_j+(b-1)/2-j:0\le j<b\}$ as a multiset, and adding a scalar shifts every member.

Choose a set $S$ containing exactly one prime of $E$ above every finite prime of $F$. Let $K'_w$ be a family of local unitary level subgroups satisfying the source's level conditions and equal to the standard subgroup almost everywhere. Let $f_w$ be Hecke test functions for $K'_w$, equal almost everywhere to the standard subgroup indicator. For every $0\le a\le n$, choose product-general-linear test functions $\varphi_{a,w}$ satisfying the source's twisted level and restricted-product test conditions and matching $f_w$ through $\mu_w$ at every $w\in S$. Then $$\mathcal G_U(S,\lambda,f)=\sum_{i\in I}s_i\,\mathcal G^{\mathrm{st}}_{a_i,n-a_i}(S,\lambda_{1,i},\lambda_{2,i},\varphi_{a_i}).$$ Here $\mathcal G_U$ and $\mathcal G^{\mathrm{st}}$ are the source's unitary geometric distribution and stable two-factor geometric distribution, with their specified masses, weight characters, orbital integrals and measures.
