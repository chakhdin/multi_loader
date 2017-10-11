LOAD DATA 
APPEND
   INTO TABLE TMP_BLOCK_HEADERS
   FIELDS TERMINATED BY ',' TRAILING NULLCOLS
   (
	BLOCK_HEADER_REF,
	VERSION,
	PREV_HASH,
	MERKLE_TREE_ROOT,
	TIME	"to_timestamp(:time, 'YYYY-MM-DD HH24:MI:SS')",
	BITS,
	NONCE,
	TX_COUNT,
	BLOCK_HASH,
	BLOCK_HEIGHT,
	BLOCK_INDEX,
	BLOCK_SIZE,
	WRITE_TIMESTAMP	"systimestamp"
	)

--sqlldr.exe userid=btc_user/btc_user@fiatdev direct=true control=../header.ctl log=../log/header.log bad=header.bad
