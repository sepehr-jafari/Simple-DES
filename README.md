# Simple-DES
Implementing DES algorithm encryption

## Implementing The Key Schedule module
<div align="justify">
The bellow algorithm specifies how to compute the DES round keys K<sub>i</sub>, each of which contains 48 bits of K. These operations make use of tables PC1 AND PC2, which are called permuted choice 1 and permuted choice 2. To begin, 8 bits of K are discarded (by PC1). the remaining 56 bits are permuted and assigned to two 28-bit variables C and D; and then for 16 iterations, both C and D are rotated either 1 or 2 bits, and 48 bits (K<sub>i</sub>) are selected from the concatenated result.
</div>

<div>
  

### PC1
|    |    |    |    |    |    |    |
|----|----|----|----|----|----|----|
| 57 | 49 | 41 | 33 | 25 | 17 |  9 |
|  1 | 58 | 50 | 42 | 34 | 26 | 18 |
| 10 |  2 | 59 | 51 | 43 | 35 | 27 |
| 19 | 11 |  3 | 60 | 52 | 44 | 36 |
| 63 | 55 | 47 | 39 | 31 | 23 | 15 |
|  7 | 62 | 54 | 46 | 38 | 30 | 22 |
| 14 |  6 | 61 | 53 | 45 | 37 | 29 |
| 21 | 13 |  5 | 28 | 20 | 12 |  4 |

### PC2
|    |    |    |    |    |    |
|----|----|----|----|----|----|
| 14 | 17 | 11 | 24 |  1 |  5 |
|  3 | 28 | 15 |  6 | 21 | 10 |
| 23 | 19 | 12 |  4 | 26 |  8 |
| 16 |  7 | 27 | 20 | 13 |  2 |
| 41 | 52 | 31 | 37 | 47 | 55 |
| 30 | 40 | 51 | 45 | 33 | 48 |
| 44 | 49 | 39 | 56 | 34 | 53 |
| 46 | 42 | 50 | 36 | 29 | 32 |

</div>
<div align="justify">

#### Algorithm DES key schedule

**INPUT**: 64-bit key K = k<sub>1</sub>...k<sub>64</sub> (including 8 odd-parity bits).  
**OUTPUT**: sixteen 48-bit keys K<sub>i</sub>, 1 ≤ i ≤ 16.

1. Define v<sub>i</sub>, 1 ≤ i ≤ 16 as follows: v<sub>i</sub> = 1 for i ∈ {1, 2, 9, 16}; v<sub>i</sub> = 2 otherwise.  
   (These are left-shift values for 28-bit circular rotations below.)
2. T ← PC1(K); represent T as 28-bit halves (C<sub>0</sub>, D<sub>0</sub>).  
   (Use PC1 to select bits from K: C<sub>0</sub> = k<sub>57</sub>k<sub>49</sub> ... k<sub>36</sub>, D<sub>0</sub> = k<sub>63</sub>k<sub>55</sub> ... k<sub>4</sub>.)
3. For i from 1 to 16, compute K<sub>i</sub> as follows:  
   C<sub>i</sub> ← (C<sub>i−1</sub> ←. v<sub>i</sub>), \( D<sub>i</sub> ← (D<sub>i−1</sub> ←. v<sub>i</sub>),  K<sub>i</sub> ← PC2(C<sub>i</sub>, D<sub>i</sub>).  
   (Use PC2 select 48 bits from the concatenation b<sub>1</sub>b<sub>2</sub> ... b<sub>56</sub>} of C<sub>i</sub> and D<sun>i</sub>; K<sub>i</sub> = b<sub>14</sub>b<sub>17</sub> ... b<sub>32</sub>. '←.' denotes left circular shift.)
  
</div>

## Implementing The DES Encryption

<div align="justify">
  DES is a Feistel cipher which processes plaintext blocks of n = 64 bits, producing 
  64-bit ciphertext bolcks. The effective size of the secret key is k = 56 bits; more   precisely, the input key K is specified as a 64-bit key, 8 bits of which (bits 8,     16, ..., 64) may be used as parity bits. The 2<sup>56</sup> keys implement (at        most) 2<sup>56</sup> of the 2<sup>64</sup>! possible bijectin on 64-bit blocks.       widely held belief is that the parity bits were introduced to reduce the effective    key size from 64 to 56 bits, to intentionally reduce the cost of exhaustive key   
  search by a factor of 256.
</div>

<div align="center">
  <img src="https://github.com/sepehr-jafari/Simple-DES/blob/main/img/DES%20Big%20Picture.PNG?raw">
</div>

<div align="justify">
  Encryption proceeds in 16 stages or rounds. From the input key K, sixteen 48-bit subkeys K<sub>i</sub> are generated, one for each round. Within each round, 8 fixed, carefully selected 6-to-4 bit substitution mapping (S-boxes) S<sub>i</sub>, collectively denoted S, are used. The 64-bit plaintext is divided into 32-bit havles L<sub>0</sub> and R<sub>0</sub>. Each round is functionally equivalent, taking 32-bit inputs L<sub>i-1</sub> and R<sub>i-1</sub> from the previous round and producing 32-bit outputs L<sub>i</sub> and R<sub>i</sub> for 1 ≤ i ≤ 16, as follows:
</div>

<div>
  L<sub>i</sub> = R<sub>i−1</sub>; <br>
  R<sub>i</sub> = L<sub>i−1</sub> ⊕ f(R<sub>i−1</sub>, K<sub>i</sub>), where         
  f(R<sub>i−1</sub>, K<sub>i</sub>) = P(S(E(R<sub>i−1</sub>) ⊕ K<sub>i</sub>))
</div>

<div align="justify">
  Here E is a fixed expansion permutation mapping R<sub>i-1</sub> from 32 to 48 bit (all bits are used once; some are used twice). P  is another fixed permutation on 32 bits. An initial bit permutation (IP) preceds the first round; following the last round, the left and right halves are exchanged and, finally, the resulting string is bit-permuted by the inverse of IP. Decrytion involves the same key and algorithm, but with subkeys applied to the internal rounds in the reverse order.<br>
  A simplified view is that the right half of each round (after expanding the 32-bit input to 8 characters of 6 bits each) carries out a key-dependent substitution on each of 8 charcters, then uses a fixed bit transposition to redistribute the bits of the resulting characters to produce 32 output bits.
  
</div>

<div align="center">
  <img src="https://github.com/sepehr-jafari/Simple-DES/blob/main/img/Feistel.PNG" title="DES Feistel structure">
  <p>DES Feistel structure</p>
</div>

<div>
  
   #### Algorithm Data Encryption Standard (DES)
   INPUT: plaintext m<sub>1</sub> ...m<sub>64</sub>; 64-bit key K = k<sub>1</sub> ...k<sub>64</sub> (includes 8 parity bits).
  OUTPUT: 64-bit ciphertext block C = c<sub>1</sub> ...c<sub>64</sub>.
  1. (key schedule) Compute sixteen 48-bit round keys K<sub>i</sub> from K using previous algrorithm.
  2. (L<sub>0</sub>, R<sub>0</sub>) ← IP(m<sub>1</sub>m<sub>2</sub> ...m<sub>64</sub>). (Use IP from below Tables to permute bits; split the
  result into left and right 32-bit halves L<sub>0</sub> = m<sub>58</sub>m<sub>50</sub> ...m<sub>8</sub>, R<sub>0</sub> = m<sub>57</sub>m<sub>49</sub> ...m<sub>7</sub>.)
  3. (16 rounds) for i from 1 to 16, compute L<sub>i</sub> and R<sub>i</sub> using previous Equations.
  above, computing f(R<sub>i−1</sub>, K<sub>i</sub>) = P(S(E(R<sub>i−1</sub>) ⊕ K<sub>i</sub>)) as follows:
  (a) Expand R<sub>i−1</sub> = r<sub>1</sub>r<sub>2</sub> ...r<sub>32</sub> from 32 to 48 bits using E in bellow tables:
  T ← E(R<sub>i−1</sub>). (Thus T = r<sub>32</sub>r<sub>1</sub>r<sub>2</sub> ...r<sub>32</sub>r<sub>1</sub>.) <br>
  (b) T'← T⊕K<sub>i</sub>. Represent T' as eight 6-bit character strings: (B<sub>1</sub>,... ,B<sub>8</sub>) =T'.<br>
  (c) T'' ← (S<sub>1</sub>(B<sub>1</sub>), S<sub>2</sub>(B<sub>2</sub>),...S<sub>8</sub>(B<sub>8</sub>)). (Here S<sub>i</sub>(B<sub>i</sub>) maps B<sub>i</sub> = b<sub>1</sub>b<sub>2</sub> ...b<sub>6</sub> to the 4-bit entry in row r and column c of S-box Tables.)<br>
  (d) T'''← P(T''). (UseP in bellow Table to permute the 32 bits of T''= t<sub>1</sub>t<sub>2</sub> ...t<sub>32</sub>, yielding t<sub>16</sub>t<sub>7</sub> ...t<sub>25</sub>.)
  4. b<sub>1</sub>b<sub>2</sub> ...b<sub>64</sub> ← (R<sub>16</sub> L<sub>16</sub>). (Exchange final blocks L<sub>16</sub>, R<sub>16</sub>.)
  5. C ← IP<sup>−1</sup>(b<sub>1</sub>b<sub>2</sub> ...b<sub>64</sub>). (Transpose using IP<sup>−1</sup> from bellow Table; C = b<sub>40</sub>b<sub>8</sub> ...b<sub>25</sub>.)
</div>

<table>
<tr><th>IP </th><th>IP<sup>-1</sup></th></tr>
<tr><td>

|    |    |    |    |    |    |    |    |
|----|----|----|----|----|----|----|----|
| 58 | 50 | 42 | 34 | 26 | 18 | 10 | 2  |
| 60 | 52 | 44 | 36 | 28 | 20 | 12 | 4  |
| 62 | 54 | 46 | 38 | 30 | 22 | 14 | 6  |
| 64 | 56 | 48 | 40 | 32 | 24 | 16 | 8  |
| 57 | 49 | 41 | 33 | 25 | 17 | 9  | 1  |
| 5  | 51 | 43 | 35 | 27 | 19 | 11 | 3  |
| 61 | 53 | 45 | 37 | 29 | 21 | 13 | 5  |
| 63 | 55 | 47 | 39 | 31 | 23 | 15 | 7  |

</td><td>

|    |    |    |    |    |    |    |    |
|----|----|----|----|----|----|----|----|
| 40 | 8  | 48 | 16 | 56 | 24 | 64 | 32 |
| 39 | 7  | 47 | 15 | 55 | 23 | 63 | 31 |
| 38 | 6  | 46 | 14 | 54 | 22 | 62 | 30 |
| 37 | 5  | 45 | 13 | 53 | 21 | 61 | 29 |
| 36 | 4  | 44 | 12 | 52 | 20 | 60 | 28 |
| 35 | 3  | 43 | 11 | 51 | 19 | 59 | 27 |
| 34 | 2  | 42 | 10 | 50 | 18 | 58 | 26 |
| 33 | 1  | 41 | 9  | 49 | 17 | 57 | 25 |

</td></tr> </table>

<table>
<tr><th>E </th><th>P</th></tr>
<tr><td>

|    |    |    |    |    |    | 
|----|----|----|----|----|----|
| 32 | 1  | 2  | 3  | 4  | 5  |
| 4  | 5  | 6  | 7  | 8  | 9  |
| 8  | 9  | 10 | 11 | 12 | 13 |
| 12 | 13 | 14 | 15 | 16 | 17 |
| 16 | 17 | 18 | 19 | 20 | 21 |
| 20 | 21 | 22 | 23 | 24 | 25 |
| 24 | 25 | 26 | 27 | 28 | 29 |
| 28 | 29 | 30 | 31 | 32 | 1  |

</td><td>

|    |    |    |    |
|----|----|----|----|
| 16 | 7  | 20 | 21 |
| 29 | 12 | 28 | 17 |
| 1  | 15 | 23 | 26 |
| 5  | 18 | 31 | 10 |
| 2  | 8  | 24 | 14 |
| 32 | 27 | 3  | 9  |
| 19 | 13 | 30 | 6  |
| 22 | 11 | 4  | 25 |

</td></tr> </table>

<div>
  The below figure demonstrate the schema of round function in DES algorithm.
</div>

<div>
  <img >
</div>
