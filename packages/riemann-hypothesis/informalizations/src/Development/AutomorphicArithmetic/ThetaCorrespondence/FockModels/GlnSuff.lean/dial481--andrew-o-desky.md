---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/GlnSuff.lean",
  "declarations": [
    "UpperTheory.Lit.Cas.casselmanSuffTemp",
    "UpperTheory.Lit.Cas.coeffLp_of_heckeWeak"
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

## A sufficient Jacquet-exponent criterion for temperedness

[Theorem REP.1458](https://andrewodesky.com/rh/lean/UpperTheory.Lit.Cas.casselmanSuffTemp/)

Assume that smooth irreducible complex representations of general linear groups over every nonarchimedean local field are admissible ([Admissibility of smooth irreducible general linear representations](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SmGLBridge.irreducibleAdmissible/)), and that normalized Jacquet modules and parabolic induction preserve finite length for positive standard block sizes ([Finite length of Jacquet modules](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.JacquetBridge.jacquetFiniteLength/) and [Finite length of parabolic induction](https://andrewodesky.com/rh/lean/GroundTheory.Automorphic.Parabolic.hasFiniteLength_parabolicInd/)). Let $k$ be such a field, $N\ge1$, and $\pi$ a smooth irreducible complex representation of $\operatorname{GL}_N(k)$. Suppose every scalar central action $\pi(t1_N)=c\,\mathrm{id}$ has $|c|=1$.

For every decomposition $N=n_1+n_2$ with $n_i>0$, let $\tau_1\boxtimes\tau_2$ be an irreducible constituent with nonzero Jordan–Hölder multiplicity in the normalized Jacquet module for those blocks. Suppose that whenever $t\in k^\times$ has $t^r\to0$ and $\tau_i(t1_{n_i})=c_i\,\mathrm{id}$, one has $$|c_1|\le1,\qquad |c_1c_2|=1.$$ Then $\pi$ has tempered matrix coefficients in the sense specified below.

## Hecke eigenvalue bounds imply integrability of matrix coefficients

[Theorem REP.1619](https://andrewodesky.com/rh/lean/UpperTheory.Lit.Cas.coeffLp_of_heckeWeak/)

Let $k$ be a nonarchimedean local field with residue cardinality $q$, $N\ge0$, and $\pi$ a smooth irreducible admissible complex representation of $G=\operatorname{GL}_N(k)$ with unitary central character. Let $K_m=\ker(\operatorname{GL}_N(\mathcal O_k)\to\operatorname{GL}_N(\mathcal O_k/\varpi^m))$ for $m\ge1$, and set $t_j=\operatorname{diag}(\varpi I_j,I_{N-j})$ for $0<j<N$. Assume every eigenvalue $\mu$ of every normalized Hecke operator for $K_mt_jK_m$ on $V^{K_m}$ satisfies $$|\mu|\le q^{-j(N-j)/2}\qquad(m\ge1;\ 0<j<N).$$ For every $p>2$, every Haar measure $dg$ on $G/Z(G)$ with its Borel measurable structure, every $v\in V$, and every complex-linear functional $\lambda$ with open stabilizer under precomposition by $\pi$, there is a real function $F\in L^p(G/Z(G),dg)$ with $$F(gZ(G))=|\lambda(\pi(g)v)|\qquad(g\in G).$$
