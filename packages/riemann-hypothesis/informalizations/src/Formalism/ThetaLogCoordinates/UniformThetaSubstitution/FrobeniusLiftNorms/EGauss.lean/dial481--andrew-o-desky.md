---
{
  "module": "src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/FrobeniusLiftNorms/EGauss.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.G7.gauss_a_one_bound"
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

## Coefficient valuations for differential minors

[Theorem PHT.1753](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.gauss_a_one_generic/)

Let $p>2$ be prime, let $\nu\ge1$ and $r_0,r_1\ge0$ be integers, and put $S=\mathbb Z/(2\nu)\mathbb Z$. Let $K$ be a field of characteristic zero with a non-archimedean absolute value $|\cdot|$ such that $|p|=p^{-1}$; the field $\mathbb C_p$ is an example. Work over $K$ with variables $Z_{s,a,b}$ for $s\in S$, $1\le a\le r_0$, $1\le b\le r_1$. Fix $u_s\in K$ with $|u_s|\le1$, and define formal series $$q_{s,a,b}=\sum_{j\ge0}(-1)^jZ_{s-2j,a,b}^{p^{2j}},\qquad h=\sum_{s,a,b}u_s q_{s,a,b}^{p}q_{s+1,a,b}.$$ Assume $F$ belongs to the following series class: there are power series $U_i$ whose coefficients have absolute value at most $1$ such that, for every monomial $Z^\beta$, $$[Z^\beta]F=\sum_{i=0}^{|\beta|}p^{-i}[Z^\beta](h^iU_i).$$

Choose $T\subset S$, numbers of columns $c_s\in\mathbb N$, column heights $h_{s,c}\le r_0$, and column-index maps $I_{s,c}:\{1,\ldots,h_{s,c}\}\to\{1,\ldots,r_1\}$; injectivity of these maps is not assumed. Introduce matrix variables $X_{s,i,a}$ and let $$Q(X,Z)=\prod_{s\in S}\prod_{c=1}^{c_s}\det\left(\sum_{a=1}^{r_0}X_{s,i,a}Z_{s,a,I_{s,c}(j)}\right)_{1\le i,j\le h_{s,c}},$$ $$J_F(X)=Q(X,\partial_Z)F\big|_{Z=0}.$$ Set $$\alpha_s=\begin{cases}\#\{c:h_{s,c}=1\},&s\in T,\\0,&s\notin T,\end{cases}\quad C_s=c_s-\alpha_s,\quad L_s=\sum_c h_{s,c}-\alpha_s,\quad D_s=\{(s'-s)_{2\nu}:s'\in T,\ s'\text{ has parity opposite to }s\},$$ where $(\cdot)_{2\nu}$ is the representative in $\{0,\ldots,2\nu-1\}$. Define $\ell_p(0)=0$ and $\ell_p(n)=1+\lfloor\log_p n\rfloor$ for $n\ge1$, and put $$\Delta=\sum_{s\in S}\{r_1\ell_p(\alpha_s)+r_0r_1\ell_p(L_s)\}+\sum_{s\in T}\ell_p(\alpha_s)^2,\qquad d_Q=\sum_{s\in S}(\alpha_s+L_s).$$ Every coefficient $b$ of $J_F$ satisfies $$v_p(b)\ge\sum_{s\in T}\sum_{\substack{e\ge1\ \mathrm{odd}\\e\notin D_s}}\left(\frac{\alpha_s}{p^e}-C_{s+e}\right)_+-\Delta+\frac{d_Q}{p^2-1},$$ where $v_p(b)=-\log_p|b|$, $v_p(0)=+\infty$, and $(z)_+=\max(z,0)$.
