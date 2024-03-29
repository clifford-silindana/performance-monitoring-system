import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"


export function SimpleOptionsInput(props) {

  return (
    <Select>
        <SelectTrigger>
            <SelectValue placeholder= {props.placeholder} />
        </SelectTrigger>
        <SelectContent>
            <SelectItem value="m@example.com">{props.selectItems[0]}</SelectItem>
            <SelectItem value="m@google.com">{props.selectItems[1]}</SelectItem>
        </SelectContent>
    </Select>
  )
}
