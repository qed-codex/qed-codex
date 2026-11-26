---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RealDataWeightVectorFamilyCore.lean",
  "declarations": [
    "GlobalTheory.Closing3.primRows3_typesSep3_alt"
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

## Properties of the theta maps of a realised rational family: Hecke equivariance, inner product identities, rationality, and separation of Hecke types

[Theorem THETA.0026](https://andrewodesky.com/rh/lean/GlobalTheory.Closing3.primRows3_typesSep3_alt/)

**Setting.** A *datum* $D$ is as in ([Datum of the construction and objects over it](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)): it has ranks $(k,m,t,n)$ with $f=2n$ and $r=k+m-1$, a CM field $E$, Hermitian spaces $X'$, $Y_j$, $V_j$, $W_j$ over $E$ and a coefficient field $\mathbb{L}\subset\mathbb{C}$. A rational family over $\mathbb L$ means the finite Hecke family of ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)), with rows $R_t$, lifts $L_{j,t}$ ($j<m$), and their types and occurrence sets. A realisation consists of the analytic data and the rational forms for the lifts in ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)). Use the notation $H_X(t)$, $H_V(j,t)$, $H_E$, $H_W(j)$ for its spaces, $H_E[p]$, $H_W(j)[p]$ for its type subspaces, $\kappa$, $\lambda_j(t,p,v)$, $\phi_j$ for its scalars, and $$\Theta_t\colon H_X(t)\to H_E,\qquad\theta_{j,t}\colon H_V(j,t)\to H_W(j)$$ for its theta maps. Faces, geometric cores and the two rationality tests are as in ([Rational families of forms, their realisations by theta maps, and the rationality test](https://andrewodesky.com/rh/lean/Formalism.IndefR.Rat.RowTest/)). Write $\mu_0$ for the distinguished tuple. Adjoints are taken for the inner products of these spaces.

**Hypotheses on the literature.**

- (L1) The fourteen statements listed in ([Fourteen statements from the literature on representations, automorphic forms and theta series, taken as hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.PrimIn.PublishedThetaConditionTheorems/)).
- (L2) *Partial Hecke $L$-functions.* For every number field $K$ and every finite set $S$ of finite places of $K$: for every Hecke character $\chi$ of $K$ with $|\chi|=1$ that is not of the form $|\cdot|^{it}$, $t\in\mathbb{R}$, there is an entire function $\Lambda$ with $\Lambda(s)=\prod_{w\notin S,\ \chi\text{ unramified at }w}(1-\chi(\varpi_w)\mathrm{N}w^{-s})^{-1}$ for $\operatorname{Re}s>1$ and $\Lambda(s)\ne0$ for $\operatorname{Re}s\ge1$; and there is an entire function $Z$ with $Z(s)=(s-1)\prod_{w\notin S}(1-\mathrm{N}w^{-s})^{-1}$ for $\operatorname{Re}s>1$ and $Z(s)\ne0$ for $\operatorname{Re}s\ge1$.

Assume (L1) and (L2). For every $\varepsilon>0$ there is $x_0$ such that the following holds. Let $D$ be a datum; let a rational family over $\mathbb{L}$ be given, with finite group $G$ and $m$ lifts, in which the Hecke operators of the second kind are indexed by lists of natural numbers; let a geometric core over $D$ be given whose coefficient field $F_c$ is made a subfield of $\mathbb{L}$; and let there be given a realisation of the family over $D$ and $F_c$, a face, for every $j<m$ a weight at stage $j+1$ in the sense of ([Cuspidal sections and their integral Fourier data](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.FormsPkg/)), for every $j<m$ and every embedding $\sigma\colon\mathbb{L}\to\mathbb{C}$ a vector in the model of the realisation at $(j,\sigma)$, and for every $j<m$ one-step geometric data of ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)) for the core and the $j$-th lift, with auxiliary twist set a singleton mapped to the base tuple. Let size data for $D$ be given with scale $(x,\varepsilon,J)$, $x\ge x_0$. Assume:

1. the given size data satisfy the numerical inequalities in ([Numerical size conditions for family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.SizesAt/)), and a record of twenty-three constants for the datum and the size data, subject to its own conditions (not expanded), exists;
2. *the first set of compatibility conditions* (fourteen clauses, listed under "Conventions");
3. *the second set of compatibility conditions*, between the geometric core, the weights, the vectors, the auxiliary records and the realisation (seven clauses, listed under "Conventions");
4. *equality of cuspidal multiplicities*: for every $j<m$, every model at infinity for $Y_0$ and every isomorphism $\Phi$ of the finite-adelic groups attached to $Y_0$ and $W_{j+1}$ of the admitted kind, every irreducible admissible representation $\sigma$ of the first group that is good for the realisation has the same cuspidal multiplicity for $Y_0$ as $\sigma\circ\Phi^{-1}$ has for $W_{j+1}$ with the model of the realisation (the notions of model, admitted isomorphism, good representation and cuspidal multiplicity are those of the formalization and were not opened);
5. the rationality test for the rows holds.

Then:

**(A) Primitive row comparisons.** The given realisation and face satisfy the primitive row comparisons in ([Analytic theta maps and primitive row comparisons](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.ExAt/)).

**(B) Separation of types.** If $p\ne p'$ are types occurring in the base row, then for every $j<m$ their transferred types have different Hecke polynomials at some allowed ordinary place of $L_{j,\mu_0}$, or different inert eigenvalues at some allowed inert-place/list index of $L_{j,\mu_0}$.

**(C) Hecke eigenvalues of the second kind under lifting.** There are maps $\mathrm{tr}_j$ ($j<m$) on functions $\mathcal{I}_0\times\{\text{lists}\}\to\mathbb{L}$ such that:

- if $p=(p_1,p_2)$ is an occurring type, $c$ a complex-valued function on pairs (place of $E$, list of integers) such that the corresponding subspace $H_E^{c}\subseteq H_E$ is non-zero and $\Theta_{\mu_0}^{*}H_E^{c}$ lies in the span of the image under $j_X(\mu_0)$ of the eigenspaces of the base row attached to $p$ for the Hecke operators of the second kind, and $x$ is a form in the good part of $L_{j,\mu_0}$ that is a simultaneous eigenvector of all Hecke operators with $\theta_{j,\mu_0}(j_V x)$ non-zero and in the subspace of $H_W(j)$ attached to $c$, then the eigenvalues of $x$ for the Hecke operators of the second kind are the values of $\mathrm{tr}_j(p_2)$;
- if two occurring types have second components that differ at some index, then so do the images of these components under each $\mathrm{tr}_j$.
