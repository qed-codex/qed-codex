---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SemiabelianSchemes/AbelianSchemeQuotients/QSurjective.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Semi.SplitExt.GtDatum",
    "ReciprocityTheory.ChartRestriction.G.Semi.SplitExt.IsGt"
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

## Split torus extensions with rigidified line coordinates

[Definition / hypothesis AV.D089](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.SplitExt/)

These data specify an extension by a split torus together with line bundles and local Laurent coordinates.

**Line bundles on the abelian quotient.** Let $S$ be a scheme, let $B/S$ be an abelian scheme, and let $X$ be a free abelian group of finite rank. Use ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)) for the abelian scheme and the split torus $T_{X,S}$. For every $\chi\in X$, choose a line bundle $L_\chi$ on $B$ with a chosen rigidification, in the sense of ([Rigidification, symmetry and translation kernels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.Rigidified/)). Write $e_B:S\to B$ for the identity section. Require the following triviality and isomorphism conditions:

1. For every $\chi,\chi'\in X$, there is a line-bundle isomorphism $L_{\chi'}\simeq L_{\chi+\chi'}\otimes L_\chi^{-1}$.
2. The line bundle $L_0$ is trivial.
3. For every $\chi\in X$, the line bundle $$m_B^*L_\chi\otimes z^*L_\chi\otimes\operatorname{pr}_1^*L_\chi^{-1}\otimes\operatorname{pr}_2^*L_\chi^{-1}$$ on $B\times_S B$ is trivial. Here $m_B$ is addition and $z:B\times_S B\to B$ is the composite of the structural map to $S$ with $e_B$.

**Local line coordinates.** Fix a basis $(\beta_k)_{k=1}^r$ of $X$. For each $k$, fix a trivializing open cover $(U_{k,a})_a$ for $L_{\beta_k}$, with local bases $\ell_{k,a}$ and invertible transition functions $g_{k,ab}$ defined by $\ell_{k,b}=g_{k,ab}\ell_{k,a}$ on overlaps. Write $r_{k,a}$ for the coordinate of the chosen rigidifying section in $e_B^*\ell_{k,a}$. For a tuple $j=(j_k)_{k=1}^r$ of chart indices, put $U_j=\bigcap_k U_{k,j_k}$.

An extension with these coordinates consists of a group scheme $G/S$, group homomorphisms $$T_{X,S}\xrightarrow{i}G\xrightarrow{q}B,$$ and units $u_{j,k}\in\Gamma(q^{-1}U_j,\mathcal O_G)^\times$, subject to the following conditions. The map $q$ is affine, flat and surjective, and $i$ identifies $T_{X,S}$ with the scheme-theoretic kernel of $q$. For every $j$ and every affine open $W\subseteq U_j$, the homomorphism $$\Gamma(W,\mathcal O_B)[X]\longrightarrow\Gamma(q^{-1}W,\mathcal O_G),\qquad e^{\beta_k}\longmapsto u_{j,k}|_{q^{-1}W},$$ with coefficient map $q^*$, is an isomorphism. Here $\Gamma(W,\mathcal O_B)[X]$ is the group algebra, with $e^\chi e^{\chi'}=e^{\chi+\chi'}$.

On $q^{-1}(U_j\cap U_{j'})$, require $$u_{j',k}=q^*(g_{k,j_kj'_k})u_{j,k}.$$ The action $a:T_{X,S}\times_S G\to G$ given by $a(t,g)=i(t)g$ preserves each inverse image $q^{-1}U_j$ and satisfies $$a^*u_{j,k}=\operatorname{pr}_T^*(e^{\beta_k})\operatorname{pr}_G^*u_{j,k}$$ on $T_{X,S}\times_S q^{-1}U_j$. Finally, if $e_G:S\to G$ is the identity section, then on $e_B^{-1}(U_j)$ the normalization is $$e_G^*u_{j,k}\,r_{k,j_k}=1.$$

For a given group scheme $G/S$, admitting such an extension structure means that there exist maps and coordinates satisfying all these requirements.
