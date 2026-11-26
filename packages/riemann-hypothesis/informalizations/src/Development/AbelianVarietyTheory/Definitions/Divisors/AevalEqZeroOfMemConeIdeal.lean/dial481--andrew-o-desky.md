---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/AevalEqZeroOfMemConeIdeal.lean",
  "declarations": [
    "GlobalTheory.CompHt.IsFrame",
    "GlobalTheory.CompHt.IsImageDeg",
    "GlobalTheory.CompHt.IsImageHeight",
    "GlobalTheory.CompHt.countVol",
    "GlobalTheory.CompHt.growth",
    "GlobalTheory.CompHt.imageDeg",
    "GlobalTheory.CompHt.imageHeight",
    "GlobalTheory.CompHt.imageIdeal",
    "GlobalTheory.CompHt.logCard",
    "GlobalTheory.CompHt.stdWt",
    "GlobalTheory.CompHt.vdm",
    "GlobalTheory.CompHt.volSlope"
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

## Asymptotic growth, volume and slope of graded sections

[Definition / hypothesis ARAK.D039](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.growth/)

These definitions associate a growth coefficient to a sequence of vector spaces, and a volume and slope to counts of sections.

**Growth.** Let $K$ be a field, let $D\in\mathbb N$, and let $V_h$ be a $K$-vector space for every $h\in\mathbb N$. Write $r_h=\dim_K V_h$ when this dimension is finite, and $r_h=+\infty$ otherwise. Define $$G_D(V)=\limsup_{h\to\infty}\frac{D!\,r_h}{h^D}\quad\text{in }[0,+\infty].$$ For $b\in[0,+\infty]$, write $b_{\mathbb R}=b$ if $b$ is finite and $(+\infty)_{\mathbb R}=0$.

**Degrees indexed by weights.** Let $\Psi$ be finite, let $N\in\mathbb N$, and suppose a $K$-vector space $S(v)$ is supplied for every $v\in\mathbb Z^{\Psi\times\{0,\ldots,N-1\}}$. Put $$D=|\Psi|\binom N2,\qquad v^{\rm std}_{\tau,i}=N-1-i,\qquad \Delta(v)=\prod_{\tau\in\Psi}\prod_{0\le i<j<N}(v_{\tau,i}-v_{\tau,j}).$$ Set $V_h=S(hv^{\rm std})$. The associated real degree at weight $v$ is $$\delta(v)=\frac{G_D(V)_{\mathbb R}}{\Delta(v^{\rm std})}\,\Delta(v).$$ The denominator $\Delta(v^{\rm std})$ is positive; empty products are one.

**Volume.** Let $D,d,a\in\mathbb N$ and, for every $n\in\mathbb N$ and $t\in\mathbb R$, let $A_n(t)$ be a set. Define $$\lambda(A)=\begin{cases}0,&A=\varnothing,\\ \log|A|,&A\text{ is finite and nonempty},\\ +\infty,&A\text{ is infinite}. \end{cases}$$ The volume sampled at multiples of $a$ is $$V_{D,d,a}(t)=\limsup_{h\to\infty} \frac{D!\,\lambda(A_{ah}(t))}{d(ah)^{D+1}}\quad\text{in }[0,+\infty].$$

**Slope.** For a real degree $\delta$ and a function $V:\mathbb R\to[0,+\infty]$, define $$s_\delta(V)=\inf_{t\in\mathbb R}\left(\frac{V(t)}{\max(\delta,0)}-t\right)\quad\text{in }[-\infty,+\infty].$$ The quotient is first taken in the nonnegative extended reals, then embedded in the extended reals before subtracting $t$.

## Image degrees and Chow heights of linear evaluations

[Definition / hypothesis ARAK.D052](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.imageIdeal/)

Let $K\subseteq\Omega$ be fields, let $V$ be a $K$-vector space, let $\operatorname{ev}:V\to\Omega$ be $K$-linear, and let $D\in\mathbb N$.

**Image degree.** For a finite basis $b=(b_j)_{0\le j<N}$ of $V$, define the homogeneous image ideal $$I_{\operatorname{ev},b}=\ker\left(K[X_0,\ldots,X_{N-1}]\longrightarrow\Omega[T],\quad X_j\longmapsto T\operatorname{ev}(b_j)\right).$$ A Chow form of dimension $D$ and block degree $\delta$ for this ideal means a polynomial over $K$ with the irreducibility, block homogeneity and incidence property stated in ([Existence of a Chow form](https://andrewodesky.com/rh/lean/GlobalTheory.ChowExists.exists_isChowFormInt/)). Define $\delta(\operatorname{ev},D)$ to be the common block degree of these Chow forms over all finite bases when any exist, and zero otherwise.

**Integral generators and norms.** Now let $K$ be a number field, give $V$ a compatible $\mathcal O_K$-module structure, and let $L\subseteq V$ be an $\mathcal O_K$-submodule. Suppose real-valued functions $N_\sigma:V\to\mathbb R$ are specified for every embedding $\sigma:K\hookrightarrow\mathbb C$, and write $\mathcal N=(N_\sigma)_\sigma$.

A frame for these data consists of a finite basis $b$ as above, a natural number $n$, a matrix $w\in M_{N\times n}(K)$ and matrices $A_\sigma\in\mathrm{GL}_N(\mathbb C)$ at every embedding. Put $\ell_k=\sum_jw_{jk}b_j$. Require $$L=\sum_{k=0}^{n-1}\mathcal O_K\ell_k,\qquad K\{w_{\cdot k}:0\le k<n\}=K^N.$$ Use the inverse-coordinate Euclidean norm of ([Rational Hermitian lattices with specified frames](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HLat/)), applied to $A_\sigma$ and a complex coordinate vector $z$; denote it by $\|z\|_{A_\sigma}$. Require $$N_\sigma(v)=\|\sigma(b^{-1}v)\|_{A_\sigma}\quad(v\in V),\qquad \|\bar z\|_{A_{\bar\sigma}}=\|z\|_{A_\sigma}\quad(z\in\mathbb C^N),$$ where $b^{-1}v$ denotes the coordinate vector of $v$ in $b$ and $\sigma$ acts entrywise. The conjugate embedding is $\bar\sigma(a)=\overline{\sigma(a)}$.

**Chow height.** For a matrix $M\in M_{N\times m}(R)$ over a commutative ring $R$ and a polynomial $f$ in $B$ blocks of $N$ variables, write $f[M]$ for blockwise substitution $$U_{ij}\longmapsto\sum_{k=0}^{m-1}M_{jk}Y_{ik}\qquad(0\le i<B,\ 0\le j<N).$$ For a finite place $v$ of $K$, use $|a|_v=(\mathrm Nv)^{-\operatorname{ord}_v(a)}$ for $a\ne0$, and define $G_v(q)$ to be the maximum absolute value of the coefficients of a polynomial $q$, with $G_v(0)=0$.

Let $\beta_{B,N}$ be the product of $B$ copies of the uniform probability measure on the Euclidean unit sphere in $\mathbb C^N$; for $N=0$ use the zero measure on the empty sphere. For a complex polynomial $q$ in these blocks put $$M_{B,N}(q)=\int\log|q(z_0,\ldots,z_{B-1})|\,d\beta_{B,N}(z_0,\ldots,z_{B-1}).$$ Write $H_j=\sum_{a=1}^j1/a$, with $H_0=0$. For any $B,N,n\in\mathbb N$, a matrix $w\in M_{N\times n}(K)$, a family $A_\sigma\in M_N(\mathbb C)$, a natural number $\delta$ and a polynomial $f$ over $K$ in $B$ blocks of $N$ variables, set $$\mathcal H_\delta(w,A;f)=\frac{1}{[K:\mathbb Q]}\left[ \sum_{v<\infty}\log G_v(f[w])+ \sum_{\sigma:K\hookrightarrow\mathbb C}\left(M_{B,N}(\sigma(f)[A_\sigma])+\frac{B\delta}{2}H_{\max(N-1,0)}\right)\right].$$ Here $\sigma(f)$ means that $\sigma$ is applied to every coefficient. The finite-place substitution has $n$ variables in each block; the archimedean substitution has $N$ variables in each block.

Fix $B=D+1$. The chosen image height $h(\mathcal N,L,\operatorname{ev},D)$ is a real number $h$ for which there are a frame $(b,w,A)$, a degree $\delta$ and a Chow form $f$ for $I_{\operatorname{ev},b}$ of dimension $D$ and block degree $\delta$, satisfying $$(D+1)\delta h=\mathcal H_\delta(w,A;f).$$ Choose such an $h$ whenever one exists, and put $h(\mathcal N,L,\operatorname{ev},D)=0$ otherwise.

For a component cusp space and generic evaluation from ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)), the component image degree is $$D_Z(u)=\delta(\operatorname{ev}_Z,d),\qquad d=|\Psi|\binom{p+q}{2}.$$
