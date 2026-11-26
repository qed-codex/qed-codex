---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/HilbertNinetyQuotientHomEqIff.lean",
  "declarations": [
    "GlobalTheory.WeilM.IsHerm",
    "GlobalTheory.WeilM.IsQuad",
    "GlobalTheory.WeilM.ResEtaPow"
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

## Local Weil data and action formulas

[Definition / hypothesis THETA.D244](https://andrewodesky.com/rh/lean/GlobalTheory.KSp.IsKW/)

Let $F$ be a nonarchimedean local field of characteristic zero and $E/F$ a quadratic field extension with its module topology and conjugation $c$. Choose $\delta\in E^\times$ such that $c(\delta)=-\delta$ and $(1,\delta)$ is an $F$-basis. Let $\alpha,\nu$ be finite index sets, put $m=|\alpha|$, and let $Q\in M_\alpha(E)$ be a nondegenerate $c$-Hermitian matrix.

Choose a continuous nontrivial additive character $\psi:F\to\mathbb C^\times$ with $|\psi(t)|=1$ and a continuous multiplicative character $\chi:E^\times\to\{z\in\mathbb C:|z|=1\}$. For $a\in F^\times$ require $$\chi(a)=\begin{cases}1,&a\in N_{E/F}(E^\times),\\(-1)^m,&a\notin N_{E/F}(E^\times).\end{cases}$$ For $a\in F^\times$, let $|a|_F$ be the positive scalar by which multiplication by $a$ scales additive Haar measure: $\lambda(aB)=|a|_F\lambda(B)$ for additive Haar measure $\lambda$ on $F$ and measurable $B\subseteq F$.

Put $V=M_{\alpha,\nu}(E)$ with its Borel measurable structure, fix an additive Haar measure $\mu$ on $V$, and let $\mathcal S(V)$ be the complex vector space of locally constant compactly supported functions on $V$. With $I_\nu$ the identity matrix indexed by $\nu$, put $$J_0=\begin{pmatrix}0&I_\nu\\-I_\nu&0\end{pmatrix},\qquad G=\{g\in\operatorname{GL}_{\nu\sqcup\nu}(E):gJ_0\bar g^{\,t}=J_0\}.$$ A bar means entrywise conjugation by $c$. Define the $F$-bilinear pairing $$\beta_Q(x,y)=\frac12\operatorname{Tr}_{E/F}\sum_{i,k\in\alpha}Q_{ik}\sum_{j\in\nu}x_{ij}c(y_{kj}).$$

For $\kappa\in\mathbb C$ and a complex-linear representation $\omega$ of $G$ on $\mathcal S(V)$, the *local Weil action formulas* are the following identities, for every $\phi\in\mathcal S(V)$ and $x\in V$. For every $p=\begin{pmatrix}A&B\\0&D\end{pmatrix}\in G$, $$[\omega(p)\phi](x)=\chi(\det A)\,|N_{E/F}\det A|_F^{m/2}\, \psi\bigl(\tfrac12\beta_Q(xA,xB)\bigr)\phi(xA).$$ For $w=J_0$, $$[\omega(w)\phi](x)=\kappa\int_V\psi(\beta_Q(x,y))\phi(y)\,d\mu(y).$$
