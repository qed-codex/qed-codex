---
{
  "module": "src/Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean",
  "declarations": [
    "Formalism.L2.Col.ChGlob",
    "Formalism.L2.Col.ChIdx",
    "Formalism.L2.Col.ChIdx.Ok",
    "Formalism.L2.Col.DecoF",
    "Formalism.L2.Col.LevI",
    "Formalism.L2.Col.Loc.E1",
    "Formalism.L2.Col.Loc.R1",
    "Formalism.L2.Col.Loc.om",
    "Formalism.L2.Col.LocCst",
    "Formalism.L2.Col.LocCst.Ok",
    "Formalism.L2.Col.LocE.JGsym",
    "Formalism.L2.Col.LocE.JQ",
    "Formalism.L2.Col.LocE.PhiGS",
    "Formalism.L2.Col.LocE.PhiQ",
    "Formalism.L2.Col.PsiAt",
    "Formalism.L2.Col.XiAt",
    "Formalism.L2.Col.XiCpl1",
    "Formalism.L2.Col.XiCpl2",
    "Formalism.L2.Col.XiEntry"
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

## Decorated lattices and auxiliary kernel characters

[Definition / hypothesis ALG.D182](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Deco/)

Hypothesis (decorated kernel lattices). Use ([Arithmetic field models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Fields/)). In this entry write $E,F,K$ for its model fields. For a prime $P$ of $E$, let $O_P=\mathcal O_{E,P}$ and $k_P=\mathcal O_E/P$. Reduction $\operatorname{red}_P:E\to k_P$ is the usual reduction on $O_P$ and zero outside $O_P$. Write $h(x,y)=\sum_i\bar x_i y_i$ on $E^n$.

For finite prime sets $T,G$, a decorated rank-$n$ lattice is a full integral lattice $N\subset E^n$, self-dual for $h$, with maps $f_P:E^n\to k_P$ for $P\in T$ and $b_P:E^n\to k_P^n$ for $P\in G$. Each map is zero outside $N_P$. On $N_P$ it is additive and satisfies $f_P(ax)=\operatorname{red}_P(a)f_P(x)$, respectively $b_P(ax)=\operatorname{red}_P(a)b_P(x)$, for $a\in\mathcal O_E$. Every $f_P$ is nonzero on some vector of $N$. Each $b_P$ maps $N$ onto $k_P^n$, and $x\in N$, $b_P(x)=0$ imply $x\in PN$. A decorated lattice with extra frames at a finite set $Q$ also has $E$-linear isomorphisms $a_P:E^n\simeq E^n$ such that $a_Px\in N_P$ if and only if $x\in O_P^n$.

A residue level at $P$ is a subgroup $H_P\subset\mathrm{GL}_n(k_P)$ with a character $H_P\to K^\times$. An integral local level is a subgroup $H_P\subset\{g\in\mathrm{GL}_n(E):gO_P^n=O_P^n\}$ with a character $H_P\to K^\times$. Families of these levels mean one such choice at each prime of the indicated finite prime set. The top integral level has the entire displayed group and the trivial character.

Let $\mathbb A_{E,f}^{F}=E\otimes_F\mathbb A_{F,f}$ with its integral subring $R=\mathcal O_E\otimes_{\mathcal O_F}\prod_v\mathcal O_{F_v}$. An auxiliary tuple relative to a set $S\subset\mathbb N$ is a character $\xi:(\mathbb A_{E,f}^{F})^\times\to K^\times$ satisfying all the following conditions. It is trivial on diagonal $E^\times$ and embedded $\mathbb A_{F,f}^\times$, has finite order, and kills $1+NR$ in $R^\times$ for some integer $N>0$. At every prime $v$ of $F$ it kills the wild subgroup consisting of integral ideles supported at $v$ and congruent to one modulo the radical of $\ell_vR$. It also kills all integral ideles supported at $v$ unless $v$ splits into two distinct primes of $E$, $Nv$ is prime, $Nv\notin v^2$, and $\ell_v\notin S$.

Define $Q_F(\xi)$ to be the primes where $\xi$ is nontrivial on integral supported ideles. For any map $s$ from primes of $F$ to primes of $E$, define $Q(\xi,s)=s(Q_F(\xi))$ when $Q_F(\xi)$ is finite and the empty set otherwise. Set $B=G\cup Q(\xi,s)$. No condition that $s(v)$ lies above $v$ is implicit in this definition.

A terminal row point is a decorated lattice of rank $N_m-1$ with $T=\varnothing$ and generator set $B$. Its extension at a word $v$ uses $N\oplus\mathcal O_E e_{\rm last}$, functionals $$f_P(x)=\operatorname{red}_P(h(\pi_v e_{\rm last},x)),\qquad b_P(x)=\bigl(b_P(x_{<\rm last}),\operatorname{red}_P(x_{\rm last}/\pi_v)\bigr)$$ on its local lattice, and zero outside it. If these maps do not satisfy all decorated-lattice conditions, the extension is defined to be the standard decorated lattice: $N=\mathcal O_E^{n+1}$, $f_P$ the last-coordinate reduction on $O_P^{n+1}$, and $b_P$ coordinatewise reduction there, with both zero elsewhere.

For decorated lattices $d,d'$ with the same functional-prime set $T$, define $\phi_T(d,d',x)$ to be one if, for every $P\in T$, $xN_P\subseteq N'_P$ and $f'_P(xy)=f_P(y)$ for every $y\in N_P$; otherwise it is zero. A frame lifted from $b_P$ is a fixed $E$-linear isomorphism $a_P$ satisfying $a_P(O_P^n)=N_P$ and $b_P(a_Px)=\operatorname{red}_P(x)$ on $O_P^n$ whenever such an isomorphism exists; an arbitrary fixed isomorphism is used otherwise.

## Local matrix models for kernel comparisons

[Definition / hypothesis REP.D192](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Loc.R1/)

Construction (local kernel matrices). Use ([Decorated lattices and auxiliary kernel characters](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Deco/)) and ([Arithmetic field models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Fields/)). Write $E,K$ for the model fields. The sizes and indices $k,r,t,r_0,n,c,n',c',j$ in the formulas below are natural numbers; in the family applications $k,r,t$ are the prescribed ranks and $r_0=\lfloor m/2\rfloor-1$. Fix a prime $P$ of $E$, put $q=NP$, and write $O=\mathcal O_{E,P}$ and $\operatorname{red}=\operatorname{red}_P$. All matrix entries outside their indicated sizes are zero; coordinate vectors with indices outside the size are zero. Natural subtraction is truncated at zero and division of natural numbers is integer division.

On $E^{n+c}$ let $U_i$ be the subspace supported in coordinates $l<n+i$, and let $\iota:E^n\to E^{n+c}$ append zeros. Define $R_{n,c}$ to consist of the automorphisms $r$ for which both $r$ and $r^{-1}$ preserve every $U_i$, fix $e_n$, and satisfy $re_{n+i}-e_{n+i}\in U_i$ for every natural $i$. Let $N_{n,c}\subset R_{n,c}$ fix $\iota(E^n)$ pointwise. For a subgroup $J\subset\mathrm{GL}_{n+c}(E)$ and $h\in\mathrm{GL}_{n+c}(E)$ put $$C(J,h)=R_{n,c}\cap hJh^{-1},\qquad P(J,h)=\{g\in\mathrm{GL}_n(E):r\iota=\iota g\text{ for some }r\in C(J,h)\},$$ $$a(r)=\sum_{i<c-1}(re_{n+i+1})_{n+i},\quad V(C,N^0)=\frac{[N^0:N^0\cap C\cap N_{n,c}]}{[C\cap N_{n,c}:N^0\cap C\cap N_{n,c}]}.$$ An infinite group index has natural-number value zero in this formula.

For an integer sequence $e_l$, put $L(e)=\{x:q^{-e_l}x_l\in O\ \forall l\}$. Define $$f_{k,c,n}(s)=\begin{cases}s&s<k,\\n+s-k&k\le s<k+c,\\s-c&s\ge k+c,\end{cases}\quad p_{k,c,n}(l)=\begin{cases}l&l<k,\\l+c&k\le l<n,\\k+l-n&l\ge n,\end{cases}$$ and $e^\epsilon_n(l)=0$ for $l<n$, $e^\epsilon_n(l)=\epsilon(l-n)$ otherwise. Write $Y_{n,c}^\epsilon=L(e^\epsilon_n)$. For $x:E^{n'+c'}\to E^{n+c}$ define its reordered scaled entries $$M_x^{\epsilon',\epsilon}(s,s')=x_{f_{k,c,n}(s),f_{k,c',n'}(s')}q^{e^{\epsilon'}_{n'}(f_{k,c',n'}(s'))-e^\epsilon_n(f_{k,c,n}(s))}.$$

At an auxiliary prime set $J^Q_{k,n,c}=\operatorname{Stab}(O^{n+c})\cap\operatorname{Stab}(L(1_{k\le l<n}))$. For a residue character $\xi:k_P^\times\to K^\times$, extend it by $\xi^0(a)=\xi(\operatorname{red}a)$ when the reduction is a unit and zero otherwise. Define $$\lambda^Q_{k,n}(h)=\xi^0(\det(h_{k+s,k+t})_{s,t<n-k})^{-1}.$$ The auxiliary test function $\Phi^Q_{k,r,c',n',c,n}(x)$ is $\xi^0(\det(M_{st})_{s,t<r})$ if all entries of $M=M_x^{0,0}$ are integral and $q^{-1}M_{st}$ is integral for $r\le s<n+c$, $t<r$; it is zero otherwise.

Here are the generator-prime groups. Put $e(l)=e^{i\mapsto i+1}_n(l)$ and $$L_s=L(e(l)+1_{s\le p_{k,c,n}(l)}),\qquad v_s=q^{e(f_{k,c,n}(s))}e_{f_{k,c,n}(s)}.$$ For any modules $M_s$, vectors $v_s$, integer $r$ and index set $A$, let $\mathcal J(M,v;r,A)$ consist of automorphisms preserving $M_s$ for every $s\in A$ and, for every $s<r$, preserving $M_s$ and satisfying $gv_s-v_s\in M_s$. Thus $$J^G_{k,r,t,n,c}=\operatorname{Stab}(Y_{n,c}^{i\mapsto i+1})\cap\mathcal J(L,v;r,\{r+it:i\ge0\}).$$ For the symmetric variant define $$s_{k,r_0}(l)=\begin{cases}l+r_0&l<k,\\l-k&k\le l<k+r_0,\\l&l\ge k+r_0,\end{cases}\quad s^{-1}_{k,r_0}(l)=\begin{cases}l+k&l<r_0,\\l-r_0&r_0\le l<r_0+k,\\l&l\ge r_0+k,\end{cases}$$ $$b(s)=\begin{cases}r_0&s=r_0+k,\\s&\text{otherwise},\end{cases}\quad L_s^S=L(e(l)+1_{b(s)\le s_{k,r_0}(p_{k,c,n}(l))}),\quad v_s^S=v_{s^{-1}_{k,r_0}(s)}.$$ The group used at a generator prime is $J^{G,S}=\operatorname{Stab}(Y_{n,c}^{i\mapsto i+1})\cap\mathcal J(L^S,v^S;r,\{r+it:i\ge0\})$ when the chosen Boolean is true, and $J^G$ when it is false.

Fix an additive residue character $\psi_0$ and multiplicative characters $\chi_i$, extended by the trivial character beyond their recorded range. For any infinite matrix $M$ define $$\lambda_j^G(M)=\psi_0\!\left(\operatorname{red}\sum_{i<r-1}M_{i,i+1}\right)\prod_{i<j}\chi_i^0\!\left(\det(M_{r+it+s,r+it+s'})_{s,s'<t}\right).$$ Define $\lambda_j^S(M)$ by replacing the additive sum by $$\sum_{i<k-1}M_{i,i+1}+\sum_{i<r-k-1}M_{k+i,k+i+1}.$$ The functions on square automorphisms are obtained by substituting $M_h^{i\mapsto i+1,i\mapsto i+1}$.

For the generator test at step $j$, let $M=M_x^{i\mapsto i+1,i\mapsto i+1}$ and $a=r+(j-1)t$. First require $M_{pp'}\in O$ for $p<n+c$, $p'<a$, and $q^{-1}M_{pp'}\in O$ for $a\le p<n+c$, $p'<a$. Require also $\operatorname{red}M_{p'p'}=1$ for $p'<r$, and $$\operatorname{red}M_{pp'}=0\quad(r\le p'<a,\ p<a,\ \lfloor(p'-r)/t\rfloor<\lfloor(p-r)/t\rfloor).$$ In the ordinary variant require $\operatorname{red}M_{pp'}=0$ whenever $p'<r$ and $p'<p<a$. In the symmetric variant replace this by the requirement for $p'<r$, $p<a$, $p\ne p'$ and $$r\le p\quad\text{or}\quad s_{k,r_0}(p')<s_{k,r_0}(p)\quad\text{or}\quad(p'=k+r_0\text{ and }p<k).$$ When all requirements hold, the ordinary test is $$\Phi^G_j(x)=\lambda^G_{j-1}(M)\,\chi_{j-1}^0(\det(M_{ss'})_{s,s'<a})^{-1};$$ the symmetric test uses $\lambda^S_{j-1}$ in this formula. Both functions are zero when a requirement fails. These explicit tests, groups and characters are the local matrix models used below.

## Local Fourier coefficients of kernel comparisons

[Definition / hypothesis REP.D190](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Loc.om/)

Construction (local Fourier coefficients). Use ([Local matrix models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Loc.R1/)), ([Decorated lattices and auxiliary kernel characters](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Deco/)), and ([Arithmetic field models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Fields/)). Write $E,K$ for the model fields, $N_j=k+j(t+1)$, $c_j=m-1-j$, and $B=G\cup Q(\xi,s)$. At $P\in B$ put $q=NP$. Use the generator matrix tests at $P\in G$ and the auxiliary tests with residue character $\xi_P$ at $P\notin G$. Residue characters are fixed multiplicative characters $\xi_P:k_P^\times\to K^\times$ with the following property, whenever one exists: for every prime $v$ of $F$ below $P$, every integral idele unit $u$ supported at $v$, every $a\in\mathcal O_E$ reducing to $\bar a\in k_P^\times$, if $u-a\in PR$ and $u-1\in P' R$ for every prime $P'\ne P$, then $\xi(u)=\xi_P(\bar a)$. If no character has this universal property, use the trivial character. Here $R$ is the integral adelic ring of ([Decorated lattices and auxiliary kernel characters](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Deco/)).

Choose $\psi_P:E\to K$, $D_P\in\mathbb N$, $s_P\in K$, values $u_{i,P}\in K$, depth integers $A,B_0,M$, and a Boolean $\epsilon$. Their laws are stated in ([Character indices and local kernel constants](https://andrewodesky.com/rh/lean/Formalism.L2.Col.LocCst/)). Let $Y_{j,P}=Y_{N_j,c_j}^{i\mapsto i+1}$ at generator primes and $Y_{N_j,c_j}^{0}$ otherwise. Let $J_{j,P}$ be $J^{G,S}$ when $P\in G$, $\epsilon$ is true, $J^G$ when $P\in G$, $\epsilon$ is false, and $J^Q_{k+j,N_j,c_j}$ otherwise. Write $\lambda_{j,P}$ for $\lambda^S_j$, $\lambda^G_j$, or $\lambda^Q_{k+j,N_j}$ with the same alternatives.

For $a\in E$, fix an integer $v_P(a)$ with $\operatorname{red}_P(a/q^{v_P(a)})\in k_P^\times$ whenever one exists, and an arbitrary fixed integer otherwise. For a residue character $\zeta$ and $u\in K$ put $$\zeta[u](a)=u^{v_P(a)}\zeta^0(a/q^{v_P(a)}).$$ At step $i$ use $\mu_{i,P}=\chi_{i,P}[u_{i+1,P}]$ at generator primes and $\xi_P^{-1}[u_{i+1,P}]$ at the other primes. Denote by $\Phi_{i,P}$ the matrix test of ([Local matrix models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Loc.R1/)) at source $(N_i,c_i)$ and target $(N_{i+1},c_{i+1})$, step $i+1$ at generator primes, and parameters $(k,r)$ at auxiliary primes.

For a function $\Phi:\operatorname{Hom}(E^a,E^b)\to K$, invertible $g,h$ of sizes $a,b$, and a local function $\mu$, set $$\Omega_{g,h}\Phi(x)=\mu(\det g)\mu(\det h)^{-1}s_P^{-b v_P(\det g)+a v_P(\det h)}\Phi(h^{-1}xg).$$ This formula is used with the augmented sizes $a=N_i+c_i$, $b=N_{i+1}+c_{i+1}$ and $\mu=\mu_{i,P}$.

The finite Fourier sum reducing augmented sizes $(a+c_a,b+c_b)$ to $(a,b)$ is defined as follows. Let $$\mathcal F=\{(l,s):0\le l<b+c_b,\ 0\le s<a+c_a,\ s\ge a,\ s-a=c_b\text{ or }[1\le s-a\text{ and }(l<b\text{ or }l-b<s-a)]\}.$$ For $x:E^a\to E^b$ and $z\in E^{\mathcal F}$, let $\widehat x_z$ have entry $z_{ls}$ on $\mathcal F$, entry $x_{ls}$ when $s<a,l<b$, entry zero when $s<a,l\ge b$, and otherwise entry $1_{l=b+s-a}$. Put $$\mathcal E_{\psi,V,w}(\Phi)(x)=w^{|\mathcal F|}\sum_{z\in V^{\mathcal F}}\Phi(\widehat x_z)\psi\!\left(-\sum_{i<c_b}(\widehat x_z)_{b+i,a+i+1}\right),\qquad V=\{j/q^A:0\le j<q^{A+B_0}\},\quad w=q^{-B_0}.$$ Write $E_{i,P}^{g,h}=\mathcal E_{\psi_P,V,w}(\Omega_{g,h}\Phi_{i,P})$. The normalized coefficient is $$X_{i,P}^{g,h}(x)=V(C(J_{i+1,P},h),N_{N_{i+1},c_{i+1}}\cap\operatorname{Stab}(Y_{i+1,P}))^{-1}E_{i,P}^{g,h}(x).$$ For the penultimate step $i=m_2$, define $\Psi_P^g(x,y)=(\Omega_{g,1}\Phi_{m_2,P})(\iota(x\operatorname{pr}_{<N_{m_2}}+y\operatorname{pr}_{N_{m_2}}))$, with source augmented by $c_{m_2}$ coordinates and target by $c_{m_2+1}$.

For a decorated point $p$ with extra $Q$-frames let $a_P(p)$ be its lifted generator frame at $P\in G$ and its supplied frame otherwise. Write $x^{p,p'}=a_P(p')^{-1}xa_P(p)$. Then $$X_i(\alpha,\beta;p,p';x)=\phi_T(p,p',x)\prod_{P\in B}X_{i,P}^{h_{i,\alpha,P},h_{i+1,\beta,P}}(x^{p,p'}).$$ Define $L_B(N;e)=\{z:q_P^{-e_P}z\in N_P\text{ for every }P\in B\}$. An auxiliary coset $Y$ at a lattice $N$ means $$Y=y+L_B(N;e_+),\quad y\in L_B(N;e_-),\qquad(e_-,e_+)=\begin{cases}(-1,0)&P\in G,\\(-M,M)&P\notin G.\end{cases}$$ Fix a representative $y_Y\in Y$ whenever $Y$ is nonempty, and zero otherwise. The first terminal coefficient is $$X^{(1)}(\alpha;p,p',Y;x)=\phi_T(p,p',x)\prod_{P\in B}\Psi_P^{h_{m_2,\alpha,P}}(x^{p,p'},a_P(p')^{-1}y_Y).$$

For a terminal row point $d$ let $\widetilde d$ be its extension at the source word $v$, let $b_P(d)$ be the lifted frame of $\widetilde d$, and let $\operatorname{pr}:E^{N_m}\to E^{N_m-1}$ discard the last coordinate. At each prime use the top matrix test $\Phi_{P}^{\rm top}$ with source $(N_{m_2+1},c_{m_2+1})$, target $(N_m-1,0)$ and generator step $m$. Define $$F_P(\eta,y)=\begin{cases}\psi_P(-\eta(y)),&P\in G,\ \eta(e_i)\in O_P\ \forall i,\\q^{-M n}\psi_P(-\eta(y)),&P\notin G,\ q^M\eta(e_i)\in O_P\ \forall i,\\0,&\text{otherwise},\end{cases}\qquad n=N_{m_2+1}.$$ The second terminal coefficient is $$X^{(2)}(p,Y,d;x)=\phi_T(p,\widetilde d,x)\prod_{P\in B}\Phi_P^{\rm top}\bigl(b_P(d)^{-1}\operatorname{pr}x a_P(p)\operatorname{pr}_{<N_{m_2+1}}\bigr)\,F_P\bigl(\pi_v^{-1}\operatorname{pr}_{N_m-1}x a_P(p),a_P(p)^{-1}y_Y\bigr).$$ The prime level for these kernels is $$\ell_v=T_v\left(\prod_{P\in B}NP\right)^{A+B_0},\qquad T\text{ in }\phi_T\text{ is the divisor set }T(v).$$

## Character indices and local kernel constants

[Definition / hypothesis REP.D189](https://andrewodesky.com/rh/lean/Formalism.L2.Col.LocCst/)

Hypothesis (kernel character indices). Use ([Local Fourier coefficients of kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Loc.om/)) and ([Local matrix models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Loc.R1/)), with their model fields $E,K$, finite set $B=G\cup Q(\xi,s)$, ranks $N_j$, local groups $J_{j,P}$, lattices $Y_{j,P}$, and coefficients $E_{i,P}^{g,h},X_{i,P}^{g,h},\Psi_P^g$. Choose the local constants $\psi_P,D_P,s_P,u_{i,P},A,B_0,M,\epsilon$ of ([Local Fourier coefficients of kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Loc.om/)). Choose also an embedding $\sigma:K\hookrightarrow\mathbb C$, $x_0\in E$, and Hecke characters $\mu_{0,j}$ of $E$ for $0\le j<m$, in the sense of ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). Require $m=m_2+2$ for a chosen natural number $m_2$.

The local constants satisfy $D_P\ge1$, $s_P^2=q_P$, $M\ge1$, $M\le A,B_0$, and $B_0\ge1$. The function $\psi_P$ obeys $\psi_P(x+y)=\psi_P(x)\psi_P(y)$ whenever $q_P^{D_P}x,q_P^{D_P}y\in O_P$, equals one on $O_P$, and satisfies $\psi_P(q_P^{-1})\ne1$. Require $x_0\in O_P$ with nonzero residue for every $P\in B$. For $a\in E,b\in\mathbb Z$ with $q_P^{D_P}a\in O_P$ and $x_0a-b/q_P^{D_P}\in O_P$, require $$\sigma(\psi_P(a))=\exp(2\pi\mathrm i b/q_P^{D_P}).$$ At generator primes require $D_P=1$ and $\psi_P(a/q_P)=\psi_{0,P}(\operatorname{red}_P a)$ for $a\in O_P$. At other primes require $D_P\ge2M$ and $D_P\ge2(m-1)+1$.

For a prime $P$ put $q_P^\xi\in K^\times$ equal to a fixed value $z$, when one exists, with this universal property: for every prime $v$ of $F$ below $P$ and every idele unit $y$ supported at $v$ whose underlying adele belongs to $R$, if $y-q_P\in P^2R$ and $y-1\in P'R$ for all $P'\ne P$, then $\xi(y)=z$. If no such value exists, set $q_P^\xi=1$. For every $0\le i<m$, require $$u_{i+1,P}=\mu_{i,P}^{-1}(q_P^\xi)^{-1}\quad(P\notin G),\qquad \sigma(u_{i+1,P})=\mu_{0,i,P}(q_P)^{-1}\sigma((q_P^\xi)^{-1})\quad(P\in G).$$ Here $\mu_{i,P}$ is the chosen algebraic uniformizer value in ([Arithmetic field models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Fields/)). At $P\in G$, for every globally integral $a\in E^\times$ with nonzero residue, require $\mu_{0,i,P}(a)=\sigma(\chi_{i,P}(\operatorname{red}_P a)^{-1})$.

For each natural $j$, choose a finite set $I_j$, automorphisms $h_{j,\beta,P}$ of $E^{N_j+c_j}$ for $\beta\in I_j,P\in B$, residue levels $(H^G_{j,\beta,P},\lambda^G_{j,\beta,P})$ at $P\in G$, and integral local levels $(H^Q_{j,\beta,P},\lambda^Q_{j,\beta,P})$ at $P\in Q(\xi,s)$, as defined in ([Decorated lattices and auxiliary kernel characters](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Deco/)). The following laws hold.

The sets $I_0,I_{m_2+1}$ each have exactly one element, and all their $h$ matrices are the identity. The initial residue level is the upper unitriangular subgroup of $\mathrm{GL}_k(k_P)$ with character $g\mapsto\psi_{0,P}(\sum_{i<k-1}g_{i,i+1})$, and the initial integral local level is the top level with trivial character. For every $i<m_2$, $\alpha\in I_i$, $\beta\in I_{i+1}$ and $P\in B$, the functions $E_{i,P}^{h_{i,\alpha,P},h_{i+1,\beta,P}}$ are unchanged when $A,B_0$ are replaced by any larger depths.

For every $i<m_2$, $\beta\in I_{i+1}$ and $P\in B$, some $\alpha\in I_i$ has the following nonvanishing property: there are $A_1,B_1$ such that the function $E_{i,P}^{h_{i,\alpha,P},h_{i+1,\beta,P}}$ with those depths is nonzero for every $A'\ge A_1,B'\ge B_1$. Two indices $\beta,\beta'\in I_{i+1}$ are equal if their matrices lie in the same double coset $R_{N_{i+1},c_{i+1}}hJ_{i+1,P}$ at every $P\in B$.

Conversely, take matrices $h_P$ at stage $i+1$. At $P\in G$ assume $h_PY_{i+1,P}=Y_{i+1,P}$. At $P\notin G$ assume $h_P^{-1}Y_{i+1,P}\subseteq Y_{i+1,P}$ and $q_P^{i+1}h_PY_{i+1,P}\subseteq Y_{i+1,P}$. If at each $P$ some $\alpha\in I_i$ has the preceding nonvanishing property with target $h_P$, then some $\beta\in I_{i+1}$ represents its double coset at every $P$. For all natural $j$ and $\beta\in I_j$, the selected $h_{j,\beta,P}$ themselves satisfy these generator stabilizer conditions and, at auxiliary primes, $h^{-1}Y_{j,P}\subseteq Y_{j,P}$ and $q_P^j hY_{j,P}\subseteq Y_{j,P}$.

The following support and translation conditions hold. At the terminal step write $e_P=1$ at generator primes and $e_P=M$ otherwise; write $f_P=0$ at generator primes and $f_P=M$ otherwise. For every $\alpha\in I_{m_2}$, $$\Psi_P^{h_{m_2,\alpha,P}}(x,y)\ne0\ \Longrightarrow\ q_P^{e_P}y\in O_P^{N_{m_2+1}},\quad q_P^A x\text{ has integral entries};$$ $$\Psi_P^{h_{m_2,\alpha,P}}(x,y+z)=\Psi_P^{h_{m_2,\alpha,P}}(x,y)\quad\text{if }q_P^{-f_P}z\text{ is integral};$$ $$\Psi_P^{h_{m_2,\alpha,P}}(x+z,y)=\Psi_P^{h_{m_2,\alpha,P}}(x,y)\quad\text{if }q_P^{-B_0}z\text{ has integral entries}.$$ For $i<m_2$ and every pair of indices, $$X_{i,P}^{h_{i,\alpha,P},h_{i+1,\beta,P}}(x)\ne0\ \Longrightarrow\ q_P^A x\text{ has integral entries},$$ and this $X$ function is invariant under adding a matrix whose entries become integral after multiplication by $q_P^{-B_0}$.

Finally put $C=C(J_{j,P},h_{j,\beta,P})$ and $H=P(J_{j,P},h_{j,\beta,P})$. Require $H\subseteq\mathrm{GL}_{N_j}(O_P)$. At auxiliary primes the chosen integral subgroup is exactly $H$. If $r\in C$ restricts to $g\in H$ on the first $N_j$ coordinates, its character is $$\lambda^Q_{j,\beta,P}(g)=\psi_P(a(r))^{-1}\lambda_{j,P}(h_{j,\beta,P}^{-1}rh_{j,\beta,P}).$$ At generator primes, a residue matrix belongs to $H^G_{j,\beta,P}$ if and only if it is the reduction on $O_P^{N_j}$ of some $g\in H$. For every $r\in C$ inducing such a $g$ and every residue matrix $\bar g$ induced by $g$, require $$\lambda^G_{j,\beta,P}(\bar g)=\psi_P(a(r))^{-1}\lambda_{j,P}(h_{j,\beta,P}^{-1}rh_{j,\beta,P}).$$
