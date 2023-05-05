SET param_block = 10000000;
;

WITH indexed_address AS
    (
        SELECT
            rowNumberInAllBlocks() AS index,
            address
        FROM
        (
            SELECT DISTINCT arrayJoin([src, des]) AS address
            FROM benchmark.all_data
             WHERE block_number >= {block:UInt64}
            ORDER BY address ASC
        )
    )
SELECT
    index_src,
    index_des
FROM benchmark.all_data AS t1
LEFT JOIN
(
    SELECT
        index AS index_src,
        address AS src_address
    FROM indexed_address
) AS t2 ON src = src_address
LEFT JOIN
(
    SELECT
        index AS index_des,
        address AS des_address
    FROM indexed_address
) AS t3 ON des = des_address
WHERE block_number >= {block:UInt64}
FORMAT RowBinary
;

