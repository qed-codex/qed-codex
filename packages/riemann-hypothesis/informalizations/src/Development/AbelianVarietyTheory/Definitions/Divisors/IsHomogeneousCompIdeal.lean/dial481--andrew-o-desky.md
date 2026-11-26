---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/IsHomogeneousCompIdeal.lean",
  "declarations": [
    "GlobalTheory.CompHt.ValFam",
    "GlobalTheory.CompHt.ValFam.patch",
    "GlobalTheory.CompHt.compDeg",
    "GlobalTheory.CompHt.compVol",
    "GlobalTheory.CompHt.compVolSlope",
    "GlobalTheory.CompHt.growthOn",
    "GlobalTheory.CompHt.latVal",
    "GlobalTheory.CompHt.recVals",
    "GlobalTheory.CompHt.smallOn",
    "GlobalTheory.CompHt.topDeg",
    "GlobalTheory.CompHt.vZero"
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

## Volume slopes of the components of a unitary moduli scheme

[Definition / hypothesis ARAK.D013](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.compVolSlope/)

The volume slope of an irreducible component of a unitary moduli scheme measures the number of integral cusp forms of small norm on that component, in the weights $hu$ for a fixed weight $u$, as $h\to\infty$. It is formed from a module of integral cusp forms, a set of small forms in each degree $h$, a volume and a degree.

**Setting.** Let $X$ be a unitary moduli scheme for a CM field $E$, of signature $(p,q)$ and level $(M,\mathfrak b,A)$, with coefficient number field $K\subset\mathbb C$. Suppose that complex uniformizations of $X$ are given at every embedding $\sigma:K\hookrightarrow\mathbb C$: a finite collection of Hermitian lattice domains $\mathcal D_c$, each with a uniformizing map from $\mathcal D_c$ to the complex framed points of $X$. These objects and the notation are those of ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)), ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)) and ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)), with $p=p_{\rm sig}$ and $q=q_{\rm sig}$; in particular $\Psi$ is the CM type and $\rho_\infty\in K$ is the chosen complex square root of $-d_{\rm mod}$. Put $$N=p+q,\qquad D_f=|\Psi|\binom N2,\qquad M'=\operatorname{lcm}(M,A),\qquad d_K=[K:\mathbb Q].$$ Let $X_K$ be the base change of $X$ to $K$, and let $Z$ be an irreducible component of $X_K$. Fix a real number $B$, called the cutoff, a real number $x$ and an integral weight $u\in\mathbb Z^{\Psi\times\{0,\ldots,N-1\}}$.

**Integral cusp forms.** For an integral weight $v$, let $S_Z(v,0)$ be the $K$-vector space of cusp forms of weight $(v,0)$ supported on $Z$, as defined in ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)) for $X$, $K$ and the given uniformizations. Its elements are scalar rules on the framed points of $X$. Let $\mathcal R$ be the ordinary integral-evaluation family of ([Finite-place valuation families and integral submodules](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)) and let $\mathcal H$ be the family of ([Hodge–Tate frames and finite-place evaluations](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.PointOver/)), both formed for $X$ and $K$. For a finite prime $\lambda$ of $K$ with residue characteristic $\ell$, put $$\mathcal V^B_\lambda=\begin{cases} \mathcal H_\lambda,&\ell\le B\text{ or }\ell\mid2\operatorname{disc}(E)M',\\ \mathcal R_\lambda,&\text{otherwise}. \end{cases}$$ This is the primewise selection of ([Finite-place valuation families and integral submodules](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)) for the families $\mathcal H$ and $\mathcal R$ and the selected-prime set of $E$, $M'$ and $B$. The module of $B$-integral cusp forms of weight $v$ on $Z$ is the associated integral $\mathcal O_K$-submodule $$\Lambda_{Z,B}(v)=\Lambda(S_Z(v,0);\mathcal V^B)=\{f\in S_Z(v,0):w(f)\ge0\text{ for every }\lambda\text{ and every }w\in\mathcal V^B_\lambda\}.$$

**Small forms.** An embedding $\sigma:K\hookrightarrow\mathbb C$ is permitted if $\sigma(\rho_\infty)=\rho_\infty$. For a permitted embedding $\sigma$, a frame over $Z$ is a pair $(c,z)$ of a domain label $c$ and a point $z\in\mathcal D_c$ such that the point of $X_K$ determined by $\sigma$ and by the image of $z$ under the uniformizing map of $\mathcal D_c$ lies in $Z$. For $f\in S_Z(v,0)$, write $N_{x,\sigma,c,v}(f,z)$ for the homogeneous norm of ([Homogeneous norms on unitary frame domains](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.homN/)) of the analytic reading of $f$ on $\mathcal D_c$. For $h\in\mathbb N$ and $t\in\mathbb R$, the set of small forms of degree $h$ is $$\mathcal A_{Z,h}(u,t)=\{f\in\Lambda_{Z,B}(hu):N_{x,\sigma,c,hu}(f,z)\le e^{ht}\text{ for every permitted }\sigma\text{ and every frame }(c,z)\text{ over }Z\}.$$

**Volume, degree and slope.** The volume of $Z$ at the weight $u$ is the function of $t\in\mathbb R$ $$V_{Z,B}(u,t)=\limsup_{h\to\infty}\frac{D_f!\,\log\#\mathcal A_{Z,8h}(u,t)}{d_K\,(8h)^{D_f+1}}\in[0,+\infty],$$ where $\log\#\mathcal A$ is the logarithm of the cardinality of $\mathcal A$ if the set $\mathcal A$ is finite and nonempty, $0$ if $\mathcal A$ is empty, and $+\infty$ if $\mathcal A$ is infinite. It is the volume of ([Asymptotic growth, volume and slope of graded sections](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.growth/)) for the sets $\mathcal A_{Z,h}(u,t)$, with dimension parameter $D_f$, coefficient degree $d_K$ and sampling integer $8$.

The degree $\delta_Z(u)$ of $Z$ at the weight $u$ is the real degree of the same page for the spaces $S(v)=S_Z(v,0)$ and the parameters $\Psi$ and $N$. Explicitly, let $v^{\rm std}$ be the weight with $v^{\rm std}_{\tau i}=N-1-i$, and let $$G_Z=\limsup_{h\to\infty}\frac{D_f!\,\dim_KS_Z(hv^{\rm std},0)}{h^{D_f}}\in[0,+\infty],$$ where an infinite dimension counts as $+\infty$. Then $$\delta_Z(u)=\gamma_Z\prod_{\tau\in\Psi}\ \prod_{0\le i<j<N}(u_{\tau i}-u_{\tau j}),\qquad \gamma_Z=\frac{G_Z}{\prod_{\tau\in\Psi}\prod_{0\le i<j<N}(j-i)},$$ with $G_Z$ replaced by $0$ if it is $+\infty$.

The volume slope of $Z$ at the weight $u$ is $$\operatorname{sl}_{Z,B}(u)=\inf_{t\in\mathbb R}\left(\frac{V_{Z,B}(u,t)}{\max(\delta_Z(u),0)}-t\right)\in[-\infty,+\infty],$$ the slope $s_{\delta_Z(u)}\bigl(V_{Z,B}(u,\cdot)\bigr)$ of ([Asymptotic growth, volume and slope of graded sections](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.growth/)). It depends on $x$ through the homogeneous norms.

If $\delta_Z(u)>0$, a real number $a$ satisfies $a\le\operatorname{sl}_{Z,B}(u)$ if and only if $$V_{Z,B}(u,t)\ge\delta_Z(u)\,(a+t)\qquad\text{for every }t\in\mathbb R.$$

## Finite-place valuation families and integral submodules

[Definition / hypothesis ARAK.D032](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)

These definitions turn families of finite-place evaluations into integral submodules.

**Valuation families.** Let $K$ be a number field, let $\mathcal F$ be a commutative $K$-algebra, and write $v_\lambda$ for the integer valuation at a finite prime $\lambda$ of $K$. A function $v:\mathcal F\to\mathbb R\cup\{+\infty\}$ has the required valuation properties at $\lambda$ if, for every $f,g\in\mathcal F$ and $a\in K^\times$, $$v(0)=+\infty,\qquad v(f+g)\ge\min(v(f),v(g)),\qquad v(fg)=v(f)+v(g),$$ $$v(af)=v_\lambda(a)+v(f).$$ The function constantly equal to $+\infty$ is allowed. A family $\mathcal V$ chooses, for each $\lambda$, a possibly empty set $\mathcal V_\lambda$ of such functions. For a $K$-vector subspace $W\subseteq\mathcal F$, its associated integral $\mathcal O_K$-submodule is $$\Lambda(W;\mathcal V)=\{f\in W:v(f)\ge0\text{ for every }\lambda\text{ and every }v\in\mathcal V_\lambda\}.$$

**Ordinary integral evaluations.** Take a moduli scheme $X$ and coefficient number field $K\subset\mathbb C$ with the moduli and coefficient-field choices of ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)) and ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)). Use the integral-framed-point definition and fixed-presentation evaluation of ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)), with $(X,K)$ in place of the original $(X_j,K_0)$. Here $\mathcal F$ is the $K$-algebra of scalar rules, with pointwise operations.

For each $\lambda$, range over all characteristic-zero complete DVRs $R$ with finite residue field, fraction fields $L$, embeddings $\iota:K\hookrightarrow L$, positive integers $e$ such that $$v_R(\iota(a))=e\,v_\lambda(a)\qquad(a\in K^\times),$$ and integral framed points $y$ over $(R,L,\iota)$. The ordinary family $\mathcal R_\lambda$ consists of all functions $$f\longmapsto v_{R,e}(f(y)),$$ where $v_{R,e}$ is the normalized extended evaluation valuation in ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)). In particular, a zero evaluation has value $+\infty$.

**Primewise selection.** Given two families $\mathcal V',\mathcal V''$ and a set $S\subseteq\mathbb N$, define $$\mathcal V^S_\lambda=\begin{cases} \mathcal V'_\lambda,&\text{some }n\in S\text{ has image in }\lambda,\\ \mathcal V''_\lambda,&\text{otherwise}. \end{cases}$$ For a set of rational primes $S$, the first case means that the residue characteristic of $\lambda$ belongs to $S$.

For a number field $E$, a positive integer $M'$ and a real $B$, the selected-prime set is $$S_B(E,M')=\{\ell:\ell\text{ is prime and }(\ell\le B\text{ or }\ell\mid2|\operatorname{disc}E|M')\}.$$ For a level $(M,\mathfrak b,A)$ of ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)), use $M'=\operatorname{lcm}(M,A)$.

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

## Quotient and remainder weights for a sequence of cusp spaces

[Definition / hypothesis AV.D243](https://andrewodesky.com/rh/lean/GlobalTheory.CompHS.WtPar/)

These conventions define the sequence of integral weights and the component image degree used in the binomial dimension estimate.
