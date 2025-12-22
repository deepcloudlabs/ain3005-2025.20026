export default function TableHeader({columns}){
    return(
        <thead>
        <tr>
            {
                columns.map( column_name =>
                    (<th key={column_name}>{column_name}</th>)
                )
            }
        </tr>
        </thead>
    )
}