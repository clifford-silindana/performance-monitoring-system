import { Card, CardContent } from "@/components/ui/card"
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import { AssessmentButton } from "../buttons/AssessmentButton";
import { Link } from "react-router-dom";

export function VideosCarousel(props) {

    const videos = props.videos;

    return (
        <Carousel
        opts={{
            align: "start",
        }}
        className="w-4/5 h-250 m-20 bg-gray-900"
        >
        <CarouselContent className = "w-full">
            {videos.map((video, index) => (
                        <CarouselItem key={index} className="lg:basis-2/5">
                            <div className="p-5 w-250">
                                <Card className = "bg-blue-500">
                                    <CardContent className="flex-col aspect-square items-center justify-center p-2 w-full">

                                        {
                                        <iframe className = "w-full h-full"
                                            src={video.url} allowFullScreen>
                                        </iframe>
                                        }
                                        <Link to = {`/hr/assessments/${video.id}/`}><AssessmentButton /></Link>
                                    </CardContent>
                                </Card>
                            </div>
                        </CarouselItem>
                    ))}
        </CarouselContent>
        <CarouselPrevious />
        <CarouselNext />
        </Carousel>
    )
}
