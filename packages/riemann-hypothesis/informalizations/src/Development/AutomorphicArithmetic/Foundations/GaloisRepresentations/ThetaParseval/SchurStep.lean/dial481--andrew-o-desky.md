---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SchurStep.lean",
  "declarations": [
    "UpperTheory.TP.IsLift",
    "UpperTheory.TP.IsLiftWt",
    "UpperTheory.TP.LocPair"
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

## Hypothesis: automorphic representations in large dimensions with prescribed weights and split local pairings

[Definition / hypothesis THETA.D094](https://andrewodesky.com/rh/lean/UpperTheory.TP.TLiftK/)

Let $E$ be a CM field with complex conjugation $c$ and maximal totally real subfield $F$. The hypothesis starts from an automorphic representation $U$ of the definite unitary group in $n$ variables over $E$. For every sufficiently large integer $d$ it asserts that there is an automorphic representation $U'$ of the definite unitary group in $d$ variables whose weights are given by a formula in the weights of $U$, and whose local components at the split places are related to those of $U$ by a pairing defined below.

**Notation.** The adele ring $\mathbb A$ of $F$, the ring $\mathbb A_E=\mathbb A\otimes_FE$, the completions $F_v$ at the finite places $v$ of $F$, elements supported at infinity, base data for $(F,E)$ and their conditions of admissibility, Hermitian data, and the properties of being Hermitian or skew-Hermitian of signature $(r,s)$ relative to base data are those of ([Setting for theta lifts between unitary groups of a CM extension: base data, Hermitian data, Weil representations, theta integrals](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.Base.IsGood/)), taken with $\sigma=c$. Base data include a character $\psi$ of $\mathbb A$, an embedding $\iota_w\colon E\to\mathbb C$ for each infinite place $w$ of $F$, and a finite set $P$ of finite places of $F$; a Hermitian datum $X$ of dimension $n$ includes a matrix $J_X\in M_n(E)$.

For an integer $r\ge0$, the definite unitary group $\mathcal U_r$ in $r$ variables over $E$, its automorphic representations, weights of length $r$ (sequences of integers $\lambda=(\lambda_0\ge\dots\ge\lambda_{r-1})$), the weights that occur in a space of functions on $\mathcal U_r$ at an embedding $E\to\mathbb C$, and the representations of $GL_r(E_u)$ that occur in such a space at a finite place $u$ of $E$ are those of ([Satake multisets and weights of definite unitary forms](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.SatU/)). A representation of a topological group on a complex vector space is smooth if the stabilizer of every vector is open.

**Split places and local characters.** Let $v$ be a finite place of $F$ and $t\colon E\to F_v$ a homomorphism of $F$-algebras. The set $\{x\in\mathcal O_E:|t(x)|_v<1\}$ is the prime ideal of a place $u_t$ of $E$ above $v$. Let $j_t\colon F_v\to E_{u_t}$ be the continuous homomorphism of rings that extends the inclusion of $F$ in $E$; the homomorphisms $GL_r(F_v)\to GL_r(E_{u_t})$ that it induces are also written $j_t$. For a homomorphism $\chi\colon\mathbb A_E^\times\to S^1$, define $$\chi_t\colon F_v^\times\to\mathbb C^\times,\qquad\chi_t(a)=\chi\bigl([j_t(a)]\bigr),$$ where, for $y\in E_{u_t}^\times$, $[y]\in\mathbb A_E^\times$ is the idele with component $y$ at $u_t$ and component $1$ at every other place of $E$. Here the finite part $\mathbb A_f\otimes_FE$ of $\mathbb A_E$ is identified with the ring of finite adeles of $E$.

**Split local pairing.** Let $n,d\ge0$ be integers, let $v$ and $t$ be as above, and let $\chi_X,\chi_W\colon\mathbb A_E^\times\to S^1$ be homomorphisms. Let $\mathcal S$ be the space of locally constant functions of compact support $M_{n\times d}(F_v)\to\mathbb C$. For $g\in GL_n(F_v)$, $h\in GL_d(F_v)$ and $\Phi\in\mathcal S$, put $$(T_{g,h}\Phi)(z)=\chi_{W,t}(\det g)\,\chi_{X,t}(\det h)\,|\det g|_v^{-d/2}\,|\det h|_v^{-n/2}\,\Phi\bigl(g^{-1}z\,(h^{-1})^{\mathsf T}\bigr),$$ where $|\cdot|_v$ is the absolute value of $F_v$ that takes the value $N(v)^{-1}$ at a uniformizer, $N(v)$ being the cardinality of the residue field. Let $(\tau,V)$ and $(\tau',V')$ be smooth irreducible complex representations of $GL_n(E_{u_t})$ and $GL_d(E_{u_t})$. A *split local pairing* of $\tau$ and $\tau'$ for $(t,\chi_X,\chi_W)$ is a nonzero complex-linear map $\beta$ from $\mathcal S$ to the space of conjugate-linear maps $V\to V'$ such that $$\beta(T_{g,h}\Phi)\bigl(\tau(j_t(g))x\bigr)=\tau'(j_t(h))\bigl(\beta(\Phi)(x)\bigr)$$ for all $g\in GL_n(F_v)$, $h\in GL_d(F_v)$, $\Phi\in\mathcal S$ and $x\in V$.

**Hypothesis.** Let $E$ be a CM field, and let base data for $(F,E)$ be given that satisfy conditions 1, 3, 4, 5 and 6 of admissibility for $c$. Suppose that $x^2=-b$ for some $x\in E$ and some integer $b>0$. Let $n\ge1$ be an integer, and let $X$ be a Hermitian datum of dimension $n$ with $J_X=1_n$ that is Hermitian of signature $(n,0)$ relative to the base data. Then there is an integer $d_0\ge0$ such that the following holds for every integer $d\ge d_0$.

Let $W$ be a Hermitian datum of dimension $d$ that is skew-Hermitian of signature $(d,0)$ relative to the base data and has $J_W=\delta 1_d$ for some $\delta\in E$. Let $\chi_X,\chi_W\colon\mathbb A_E^\times\to S^1$ be continuous homomorphisms that are trivial on $E^\times$, and let $m_X(w)$ and $m_W(w)$ be integers, one for each infinite place $w$ of $F$. Suppose that, for every $a\in\mathbb A^\times$, $$\chi_X(a)=\eta(a)^n,\qquad\chi_W(a)=\eta(a)^d,\qquad\eta(a)=\begin{cases}1,&a\in F^\times N(\mathbb A_E^\times),\\-1,&\text{otherwise},\end{cases}$$ where $N\colon\mathbb A_E\to\mathbb A$ is the norm, and that, for every $z\in\mathbb A_E^\times$ such that $z-1$ is supported at infinity, $$\chi_X(z)=\prod_w\Bigl(\frac{\iota_w(z)}{|\iota_w(z)|}\Bigr)^{m_X(w)},\qquad\chi_W(z)=\prod_w\Bigl(\frac{\iota_w(z)}{|\iota_w(z)|}\Bigr)^{m_W(w)},$$ the products being over the infinite places $w$ of $F$. Let $U$ be an automorphic representation of $\mathcal U_n$ and, for each infinite place $w$ of $F$, let $\lambda_w$ be a weight of length $n$ that occurs in $U$ at $\iota_w$. Suppose that $$d+m_W(w)\le2\lambda_{w,k}\qquad\text{for all }w\text{ and all }0\le k<n.$$ Then there is an automorphic representation $U'$ of $\mathcal U_d$ with the following two properties.

1. For every infinite place $w$ of $F$, a weight $\lambda'$ of length $d$ occurs in $U'$ at $\iota_w$ such that, for $0\le k<d$, $$2\lambda'_k=n+m_X(w)+\begin{cases}2\lambda_{w,k}-d-m_W(w),&k<n,\\0,&k\ge n.\end{cases}$$
2. Let $v$ be a finite place of $F$ and $t\colon E\to F_v$ a homomorphism of $F$-algebras. Let $\tau$ be a smooth irreducible complex representation of $GL_n(E_{u_t})$ that occurs in $U$ at $u_t$, and $\tau'$ a smooth irreducible complex representation of $GL_d(E_{u_t})$ that occurs in $U'$ at $u_t$. Then there is a split local pairing of $\tau$ and $\tau'$ for $(t,\chi_X,\chi_W)$.
