export default function TableData({cellkey,value}) {
    return (
        <td key={cellkey}>{value}</td>
    );
}