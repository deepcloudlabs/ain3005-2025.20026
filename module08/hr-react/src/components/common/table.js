import TableHeader from "./table-head";
import TableRow from "./table-row";

export default function Table({column_names,items,fields}) {
    return(
      <table className="table table-hover table-striped table-bordered table-responsive">
          <TableHeader columns={column_names} />
          <tbody>
          {
              items.map( (item,index) =>
                  (<TableRow key={index} rowkey={index} fields={fields} value={item}></TableRow>)
              )
          }
          </tbody>
      </table>
    );
}