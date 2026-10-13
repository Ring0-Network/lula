# Total input completion for counter-guess lift9c1f

The first counter-guess successor9c1f is preserved. To specify a TOTAL ordinary fixed-input-length family rather than just valid encoded source messages, fix a source message ceiling B bytes and use an input register of40+B bytes. Valid Enc is S16||T16||c4||length4||M||zero^(B-|M|), with length<=B and required zero padding. Decoding is injective, including trailing-zero messages. For valid inputs the virtual family executes EXACT original source h words and returns153 real-index bits followed by256 context bits and41 route bits.

For every invalid codeword X, define the450-bit output explicitly as prefix450 of

h(R16||0xff||X||0x00) || h(R16||0xff||X||0x01).

This is a public deterministic total completion using the SAME full h. It is not an extra source hash call: source B only queries valid Enc inputs. Invalid-keyword handling nevertheless belongs to the chosen full primitive family, and any assumed ITSR advantage must cover it. No independence or actual hardness of this completion is asserted. All its aliases and its two-hash/circuit costs are explicit. A deliberately weak completion would yield a weak/vacuous primitive assumption but would not invalidate the source-to-primitive inequality.

This fixes the formal-domain issue when using the primary fixed-alpha bit-string prototype for variable-length source messages. It does not change literal inner/outer source bytes, the guess-independent source view, q_distinct target queries,17-witness proof or2^544 loss. A different message-length ceiling requires a separately stated primitive instance and byte/runtime envelope.
