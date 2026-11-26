---
{
  "module": "src/Formalism/SharpRestriction/GlobalSchurBounds/TieGlobal.lean",
  "declarations": [
    "Formalism.MainNotions.ChainTied"
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

## Counting data tied to an arithmetic family

[Definition / hypothesis ANT.D030](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ChainTied/)

An arithmetic family has tied counting data at a real number $x$ when the hypotheses of ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)) hold for data that are read off from members of the family at $x$: one member for every element of the group of a base member. The condition is the family form of Hypothesis (counting conditions) of ([Character and counting conditions at a single scale](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/)).

**The family and its members.** Let $\varepsilon>0$ and let $\mathcal F$ be an arithmetic family with exponent $\varepsilon$, as in ([Arithmetic families with local and theta data](https://andrewodesky.com/rh/s/family-arithmetic-data.html)), with member sets $I_x$. For a member $i$ we use the following of its data.

- From ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)): the labelled group $A$ of order $n$ with $a_0$, $\vartheta$ and $e$; the ranks $k,m$; the primes $q,d$ and the generator primes $g_0,g_1$; the root discriminant $\operatorname{rd}_E$; the sets $T\subseteq A$ and $T_2\subseteq\mathbb Z_{\ge0}$; the shift $a_*\in A$; the subgroup $G_d$ and the set $\Sigma$ of embeddings, with the chosen $\phi_0\in\Sigma$. The label of an element of $A$ is its number in $\{0,\dots,n-1\}$.
- Its internal scale $x_i>1$, and the numbers $$L_i=x_i^\varepsilon,\qquad b_i=e^{L_i},\qquad a_i=x_ib_i,\qquad X'_i=\exp(x_i^{\varepsilon/3}),\qquad b'_i=a_i/X'_i,\qquad X''_i=nx_iX'_i.$$
- From ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)): the coefficient number field $K$, the integer weights $a_v,b_v$ for $v\in T$, the positive real number $\eta$, and the entries $E_{\tau,j}$, with $\tau\in\Sigma$ and $0\le j<m$, of its weight arrays, which are defined in ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)); these entries do not depend on the source.
- From ([Local size and support data](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.SizeData%E2%82%82/)): the finite source set, the source prime $T_z$ of a source $z$, the finite set $\mathcal S$ of finite places of $K$, the set $\mathcal D$ of discarded primes, and the real numbers $\gamma_{j,w},F_{j,w},E_{z,j,w},\tau_w,\iota_w$. For a finite place $w$ of $K$ with prime ideal $\mathfrak p_w$, residue characteristic $p_w$ and ramification index $e_w$ over $\mathbb Q$, put $$\ell_w=\frac{\log\operatorname{Norm}\mathfrak p_w}{[K:\mathbb Q]},\qquad s_w(y)=2\ell_we_wy\quad(y\in\mathbb R).$$
- From Hypothesis (source and target lattice data) of ([Hermitian row lattices and their rational models](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivData/)): the target lattice $R$, the source lattices $N_z$ and the heights $h_z$. From ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)): the Hermitian lattice $\mathcal L_0$ of every source $z$, written $\mathcal L_{z,0}$. From ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)): the real number $\delta\le1$.

For a Hermitian lattice $\mathcal L$ over $K$ write $\operatorname{rk}\mathcal L$ for the dimension over $K$ of its span, $\mu(\mathcal L)$, $\mu_{\max}(\mathcal L)$ and $\mu_{\min}(\mathcal L)$ for its mean, maximal and minimal slopes, and $\mathcal L^\vee$ for the dual lattice with the dual basis and the dual archimedean matrices.

**Hypothesis (tied counting data).** Let $x\ge1$ and let $E_D,E_P,K,C_*,e_K,C_L$ be real numbers. The family $\mathcal F$ has tied counting data at $x$ with constants $E_D,E_P,K,C_*,e_K,C_L$ when there exist

- a member $i_{\rm b}\in I_x$, called the base member, whose data $A,a_0,q,d,E,\ldots$ are taken as the field in ([Character and counting conditions at a single scale](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/)), with the notation $H=A$, $H_0$, $n$, $G$, $\Phi$, $\widehat G$, $\rho$, $I_p$, $F_p$, $a_\gamma$, $g^\kappa_\gamma$ of ([Character and counting conditions at a single scale](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/));
- a member $i_u\in I_x$ for every $u\in H$, and two functions $\alpha_1,\beta_1:\mathbb Z_{\ge0}\to\mathbb Z$;
- sets $T,T_2\subset H$, integers $m,N\ge0$, real numbers $a_t$ for $t\in H$, a function $w:H\times\{0,\dots,m-1\}\times G\to\mathbb R$ with $w_{h,j}=w(h,j,\cdot)$, a function $\kappa:\widehat G\to\mathbb C$, and real numbers $\eta,X',\theta$;
- values of all the other real parameters, constants and indexed real numbers that occur in ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)), for the index set $U=H$, the identity map $\tau$ of $H$, and $W_u$ the source set of the member $i_u$;

with the properties A to E. In these properties the data of the member $i_u$ that could be confused with the data above carry the index $u$: its ranks $k_u,m_u$, its sets $T^{(u)}\subseteq A$ and $T_2^{(u)}\subseteq\mathbb Z_{\ge0}$, its root discriminant $\operatorname{rd}_u$, its generator primes $g_{0,u},g_{1,u}$, its number $\eta_u$, its internal scale $x_u$ and the numbers $L_u,b_u,a_u,X'_u,b'_u,X''_u$ formed from it. Its lattices, heights, source primes and local size data are written $R$, $N_z$, $h_z$, $\mathcal L_{z,0}$, $T_z$, $\delta$, $\mathcal S$, $\mathcal D$, $\gamma_{j,w}$, $F_{j,w}$, $E_{z,j,w}$, $\tau_w$, $\iota_w$ without index.

A. The members. For every $u\in H$: the member $i_u$ has the same labelled group $A$, element $a_0$, homomorphism $\vartheta$ and integer $e$ as $i_{\rm b}$; its rank $m_u$ is the integer $m$ above; its primes $q,d$ are those of $i_{\rm b}$; its shift $a_*$ is $u$; and its integer weights are $a_v=\alpha_1(l)$ and $b_v=\beta_1(l)$ for every $v\in T^{(u)}$, where $l$ is the label of $v$.

B. The sets, the numbers $a_t$, the weights and $\kappa$.

1. $T$ is the set $T\subseteq A$ of the base member $i_{\rm b}$.
2. For every $u\in H$, $T_2=\{sa_0:s\in T_2^{(u)}\}$.
3. $a_t=\alpha_1(l)$ for every $t\in H$, where $l$ is the label of $t$.
4. Let $u\in H$, $0\le j<m$ and $g\in G_d$, and let $\rho_g\in\Phi$ be the element that corresponds to $g$ under the identification of $\{\pm1\}^2\times A$ with $G$. Then $w_{u,j}(\rho_g)=E_{\tau,j}$, where $\tau=\phi_0\circ\sigma_g$ and $E_{\tau,j}$ is the entry of the weight arrays of the member $i_u$; this entry is the same for all sources.
5. Property 1 of Hypothesis (counting conditions) of ([Character and counting conditions at a single scale](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/)) holds for $\kappa$.

C. The parameters of ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)). Its parameters $x$ and $\varepsilon$ are the given ones. Its parameters $a,b,b',k,L,\Lambda,B_0,N_c,v,\lambda_g,X''$ and the numbers $\eta,X'$ satisfy, for every $u\in H$, $$a=a_u,\qquad b=b_u,\qquad b'=b'_u,\qquad L=L_u,\qquad X''=X''_u,\qquad X'=X'_u,\qquad k=k_u,\qquad\eta=\eta_u,$$ $$\Lambda=\log(a_u\operatorname{rd}_u),\qquad B_0=2nm_ub_uL_u,\qquad N_c=\frac{|T_2^{(u)}|\,k_u\,b_uL_u}{n\cdot nx_u^{-\varepsilon}},$$ $$v=\tfrac12\operatorname{rd}_u,\qquad\lambda_g=\log(g_{0,u}g_{1,u}),\qquad\Re\kappa(\chi_C)=\Re\frac{L'(1,\chi_d)}{L(1,\chi_d)},$$ where $\chi_C\in\widehat G$ is the character $((\alpha',\beta'),h)\mapsto(-1)^{\alpha'}$ and $\chi_d$ is the quadratic character $r\mapsto(r/d)$ modulo $d$.

D. The indexed numbers of ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)). For every $u\in H$ and every source $z$ of the member $i_u$, $$d_{u,z}=\operatorname{rk}N_z,\qquad T_{u,z}=T_z,\qquad h_{u,z}=h_z,$$ $$\mu^N_{u,z}=\mu(N_z),\qquad\mu^{N,+}_{u,z}=\mu_{\max}(N_z),\qquad\mu^M_{u,z}=\mu(\mathcal L_{z,0}),\qquad\mu^{M,+}_{u,z}=\mu_{\max}(\mathcal L_{z,0}),$$ $$E_{u,z}=\sum_{j=1}^m\sum_{w\in\mathcal S}s_w(E_{z,j,w}),$$ and $$\mu^C_u=\mu(R^\vee),\qquad\mu^{C,-}_u=\mu_{\min}(R^\vee),\qquad\delta_u=\delta,$$ $$F_u=\sum_{j=1}^m\sum_{w\in\mathcal S}s_w(F_{j,w}),\qquad G_u=\sum_{w\in\mathcal S}s_w\Bigl(\sum_{j=1}^m\gamma'_{j,w}-\tau_w\Bigr),\qquad I_u=\sum_{w\in\mathcal S}\ell_we_w\iota_w,$$ where $\gamma'_{j,w}=0$ if $p_w\in\mathcal D$ and $\gamma'_{j,w}=\gamma_{j,w}$ otherwise.

E. The conditions.

1. All eleven numerical conditions of ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)) hold, and so do the first six of its seven size conditions, for the group $H$, the numbers $q,d$, the subgroups $I_p$ and elements $F_p$, the cutoff $N$, the function $\kappa$, the index set $H$ with the identity map, the sets $W_u$, the sets $T,T_2$, the integer $m$, the numbers $a_t$ with $t\in T$, the function $w$, and the given numbers $x,\varepsilon,K,e_K$. Its constants satisfy $e_D\le E_D$, $e_P\le E_P$ and $c_*\le C_*$.
2. Property 3 of Hypothesis (counting conditions) of ([Character and counting conditions at a single scale](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/)) holds with its conditions on the functions $w_{u,j}$ required for every $u\in H$, and so do properties 4, 5 and 6 of Hypothesis (counting conditions).
3. Let $\gamma_q\in\widehat G$ be the character $((\alpha',\beta'),h)\mapsto(-1)^{\beta'}$. For each of the three characters $\gamma\in\{\gamma_q,\chi_C,\gamma_q\chi_C\}$, $$|g^\kappa_\gamma(x)|\le x^{1/2+\varepsilon},\qquad|\kappa(\gamma)|\le C_L\log x.$$
