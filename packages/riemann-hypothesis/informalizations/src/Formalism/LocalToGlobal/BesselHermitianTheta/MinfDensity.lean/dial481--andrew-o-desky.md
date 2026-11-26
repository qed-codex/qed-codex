---
{
  "module": "src/Formalism/LocalToGlobal/BesselHermitianTheta/MinfDensity.lean",
  "declarations": [
    "Formalism.L2.Theta.RealTied",
    "Formalism.L2.Theta.ThetaTied"
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

## Automorphic theta functions and their measures

[Definition / hypothesis ARAK.D222](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)

Use ([Hermitian theta spaces and pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThetaX/)) and ([Analytic realizations of rational Hecke families](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.BaseW/)). Write $G_V=U(V)(\mathbb A_F)$, $\Gamma_V=U(V)(F)$ and $G_{V,f}$ for the subgroup with identity infinite part. Its lattice $L_V$ is the prescribed integral lattice in ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). Use the definition of a compatible family in the Character conditions section of ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)) for the infinite embeddings.

Hypothesis (automorphic theta realization). For every Hermitian space $V$, choose an injective complex-linear map $e_V:\mathcal A(V)\to\{G_V\to\mathbb C\}$. Every image is continuous, left $\Gamma_V$-invariant, and invariant on the right by the finite-part elements of some open subgroup. Membership in $\mathcal C(V)$ is equivalent to the constant-term vanishing condition in ([Analytic realizations of rational Hecke families](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.BaseW/)). Choose an isomorphism from the abstract group of finite adelic actions in ([Hermitian theta spaces and pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThetaX/)) to $G_{V,f}$. It carries the abstract finite action to right translation.

Compatible infinite embedding families exist. For every such family, every $\tau$ and every matrix $g$ preserving the embedded Gram form, an adelic element with infinite matrix $g$ at $\tau$, identity at the other infinite places and trivial finite part exists. Every such element implements the abstract $\tau$-action by right translation. The subgroup $K^S(V)$ corresponds exactly to finite adelic elements preserving $\widehat L_V$ and equal to the identity at every $v\in S$. The abstract conjugation becomes pointwise complex conjugation under $e_V$.

Choose positive real numbers $p_f(V)$ and $p_\infty(p,q)$, with $p_\infty(N,0)=p_\infty(0,N)=1$. For $p,q>0$ require $p_\infty(p,q)\mu^{\rm cd}_{p,q}$ to have infinitesimal density $2^{-(p+q)(p+q-1)/2}$ relative to the Lie algebra Lebesgue measure in ([Formal degree with compact-dual normalization](https://andrewodesky.com/rh/lean/PositivityTheory.RgFd.B.formalDegreeCompactDual/)). Put $$p(V)=p_f(V)\prod_\tau p_\infty(p_\tau,q_\tau).$$ Call a Haar measure $\nu_V$ compatible when the following rectangle identity holds for every compatible infinite embedding family, every family of matrices $A_\tau$ with $A_\tau^*J_{p_\tau,q_\tau}A_\tau=G_{V,\tau}$ and all measurable $B_\tau\subset U(p_\tau,q_\tau)$: $$\nu_V\{g:g_f\widehat L_V=\widehat L_V,\ \forall\tau\ \exists b_\tau\in B_\tau:\ b_\tau A_\tau=A_\tau g_\tau\}=\prod_\tau\mu^{\rm cd}_{p_\tau,q_\tau}(B_\tau).$$ For each compatible infinite embedding family at least one such matrix family exists; the rectangle identity holds for every such family. A rational fundamental domain means a fundamental domain for the left action of $\Gamma_V$. Whenever the specified signatures agree with the Gram signatures, compatible measures exist and every one has a rational fundamental domain. Every such domain $\mathcal F_V$ has $\nu_V(\mathcal F_V)=\operatorname{vol}(V)$, the specified volume of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). For every $V$ with correct Gram signatures, every compatible measure and domain, and all $F\in\mathcal A(V)$ and $G\in\mathcal C(V)$, $$P_V(F,G)=p(V)\int_{\mathcal F_V}\overline{e_VF(h)}e_VG(h)\,d\nu_V(h).$$ If $i:B\to A$ is isometric, $B$ has correct Gram signatures and $s:G_B\to G_A$ acts on $i(B)$ as its argument and fixes $i(B)^\perp$ pointwise, require $$B_i^{\rm top}(\phi,F)=p(B)\int_{\mathcal F_B}\overline{e_A\phi(s(h))}e_BF(h)\,d\nu_B(h)$$ for every $\phi\in\mathcal A(A)$ and $F\in\mathcal C(B)$.

Choose an injective homomorphism from the abstract character group $\mathcal X$ to continuous unitary Hecke characters of $E$. Its image consists exactly of those characters of rational infinity type. For each character and every compatible infinite embedding family, its value on an idele with finite part one and all infinite components except $\tau$ equal to one is $(z/|z|)^{2\nu_\tau}$, where $2\nu_\tau$ is an integer. Every designated $\chi_{\mu,j}$, $1\le j\le m$, restricts trivially to $\mathbb A_F^\times$. The designated $\eta$ has infinity type $1/2$, is trivial on all finite integral units, and restricts to every continuous nontrivial character of $\mathbb A_F^\times/F^\times$ trivial on norms from $\mathbb A_{E/F}^\times$. Such a quadratic norm character exists.

For every $t'\in\mathbb N$ and $0\le j\le m$, $X_{t',j}$ is positive definite and $$\operatorname{sig}_\tau Y_{t',j}=\left(r+jt'-\left\lfloor\frac{m-j}{2}\right\rfloor,\left\lfloor\frac{m-j}{2}\right\rfloor\right).$$ All arithmetic in these ranks is natural-number arithmetic.

For every natural $t',j,i$, whenever $Y_{t',j}$ has an independent isotropic $i$-frame, require $\dim Y^-_{t',j,i}+2i=\dim Y_{t',j}$ and require $Y^-_{t',j,i}$ to have correct Gram signatures and to embed isometrically in $Y_{t',j}$ orthogonally to some independent isotropic $i$-frame.

Require the measure reindexing and uniqueness of designated formal degrees in ([Period, measure and twist comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Ties/)). Require also existence, at every CM place, of a discrete-series representation with the designated moment parameter and formal degree $d_\tau$ for the scaled moment Haar measure. The parameter, sign vector, Hilbert representation conditions and four-coefficient formal-degree identity are exactly those in ([Period, measure and twist comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Ties/)); the designated rank is $2r_S+k+1$ and its alternating signed parameter is the one of ([Moment data for the family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Draft.SData/)).
