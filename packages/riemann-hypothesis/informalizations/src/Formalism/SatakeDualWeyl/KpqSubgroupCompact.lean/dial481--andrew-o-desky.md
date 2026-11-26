---
{
  "module": "src/Formalism/SatakeDualWeyl/KpqSubgroupCompact.lean",
  "declarations": [
    "Formalism.UG.Final.AdelicStabFiniteL",
    "Formalism.UG.Final.ClassSetFiniteL",
    "Formalism.UG.Final.HeckeCommGL",
    "Formalism.UG.Final.SatakeInert",
    "Formalism.UG.Final.SatakeTj"
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

## Finiteness of a definite unitary class set for any full lattice

[Theorem ANT.0195](https://andrewodesky.com/rh/lean/Formalism.UG.Final.ClassSetFiniteL/)

Let $F,E$ be number fields with $F\subseteq E$, and let $\sigma:E\to E$ be an $F$-algebra automorphism satisfying $\tau(\sigma x)=\overline{\tau(x)}$ for every embedding $\tau:E\hookrightarrow\mathbb C$. Let $J\in M_n(E)$, $n\ge0$, be nonsingular and $\sigma$-Hermitian. Suppose $F$ is totally real and, at every embedding $F\hookrightarrow\mathbb R$, the form $$h(x,y)=\sigma(x)^tJy$$ is either positive definite or negative definite, with its diagonal values in $F$.

Let $\Lambda\subset E^n$ be a finite $\mathcal O_E$-module spanning $E^n$, and let $K_\Lambda$ be the stabilizer of its completed finite-adelic lattice in $U(J)(\mathbb A_{F,f})$. Then $$U(J)(F)\backslash U(J)(\mathbb A_{F,f})/K_\Lambda$$ is finite.

## Finiteness of stabilizers of definite adelic lattice classes

[Theorem ANT.0239](https://andrewodesky.com/rh/lean/Formalism.UG.Final.AdelicStabFiniteL/)

Let $F,E$ be number fields with an $F$-algebra structure on $E$, and let $\sigma:E\to E$ be an $F$-algebra endomorphism such that $$\tau(\sigma(a))=\overline{\tau(a)}\qquad(a\in E,\ \tau:E\hookrightarrow\mathbb C).$$ Let $n\ge0$ and $J\in M_n(E)$ satisfy $\sigma(J)^t=J$ and $\det J\ne0$. Suppose $F$ is totally real and, at every real embedding $\iota:F\hookrightarrow\mathbb R$, the form $$h(x,y)=\sigma(x)^tJy$$ is definite in the following sense: either every $h(x,x)$ for $x\ne0$ is the image of an $a\in F$ with $\iota(a)>0$, or every such value is the image of an $a\in F$ with $\iota(a)<0$.

Let $\Lambda\subseteq E^n$ be a finitely generated $\mathcal O_E$-module spanning $E^n$. Put $G=U(J)$, let $K_\Lambda\subseteq G(\mathbb A_{F,f})$ be the stabilizer of its integral adelic extension, and embed $G(F)$ by rational matrices. For every $g\in G(\mathbb A_{F,f})$, $$\{\gamma\in G(F):g^{-1}\gamma g\in K_\Lambda\}$$ is finite.

## The Hecke eigenvalue of an inert unitary spherical function

[Theorem REP.0251](https://andrewodesky.com/rh/lean/Formalism.UG.Final.SatakeInert/)

Let $L$ be a complete discretely valued field with additive valuation $\operatorname{ord}$, let $\varpi\in L$ have valuation one, and let $\sigma:L\to L$ be a valuation-preserving involution fixing $\varpi$. Assume there is $x\in\mathcal O_L$ with $\operatorname{ord}(\sigma(x)-x)=0$, and the residue field has cardinality $q^2$, where $q\ge2$ is an integer. Let $2m\le n\le2m+1$, put $J_{ij}=1$ if $i+j=n-1$ and $J_{ij}=0$ otherwise, and set $$G=\{g\in\operatorname{GL}_n(L):\sigma(g)^tJg=J\},\qquad K=G\cap\operatorname{GL}_n(\mathcal O_L).$$ Let $U$ be the upper unitriangular subgroup of $G$. Choose $\alpha_0,\ldots,\alpha_{m-1}\in\mathbb C^\times$. For upper triangular $b\in G$, write $$\chi_\alpha(b)=\prod_{i=0}^{m-1}\alpha_i^{\operatorname{ord}(b_{ii})}q^{-\operatorname{ord}(b_{ii})(n-1-2i)}.$$ Suppose $\phi:G\to\mathbb C$ satisfies $\phi(bgk)=\chi_\alpha(b)\phi(g)$ for every such $b$, $g\in G$, and $k\in K$. For a $K$-bi-invariant function $h:G\to\mathbb C$ supported on finitely many double cosets, define $$(h\cdot\phi)(g)=\sum_{xK\in G/K}h(x)\phi(gx).$$ Then $h\cdot\phi=S_h(\alpha)\phi$, with $S_h$ defined below.

## Elementary spherical Hecke eigenvalues

[Theorem AGR.1068](https://andrewodesky.com/rh/lean/Formalism.UG.Final.SatakeTj/)

Let $F$ be a number field, $v$ a finite place, $q=\#(\mathcal O_F/v)$, and $\varpi\in F_v$ a uniformizer. Let $n\ge0$, $K=\mathrm{GL}_n(\mathcal O_v)$, and $\alpha_0,\ldots,\alpha_{n-1}\in\mathbb C^\times$. Suppose $\phi:\mathrm{GL}_n(F_v)\to\mathbb C$ satisfies $$\phi(bgk)=\left(\prod_{i=0}^{n-1}\alpha_i^{v(b_{ii})}q^{-v(b_{ii})(n-1-2i)/2}\right)\phi(g)$$ for every invertible upper triangular $b$, every $g$, and every $k\in K$. For $0\le j\le n$, put $a_j=\operatorname{diag}(\varpi I_j,I_{n-j})$. Then $$\sum_{xK\in Ka_jK/K}\phi(gx)=q^{j(n-j)/2}e_j(\alpha_0,\ldots,\alpha_{n-1})\phi(g)\qquad(g\in\mathrm{GL}_n(F_v)).$$

## Commutativity of the spherical Hecke algebra

[Theorem REP.1194](https://andrewodesky.com/rh/lean/Formalism.UG.Final.HeckeCommGL/)

Let $F$ be a number field, $v$ a finite place, $n\ge0$, and $R$ a commutative coefficient ring. Put $K=\operatorname{GL}_n(\mathcal O_{F_v})$. For any two $R$-valued, $K$-bi-invariant functions $f_1,f_2$ on $\operatorname{GL}_n(F_v)$ supported on finitely many double cosets, $$f_1*f_2=f_2*f_1.$$ Convolution is the finite coset sum $(f_1*f_2)(g)=\sum_{xK}f_1(x)f_2(x^{-1}g)$.
